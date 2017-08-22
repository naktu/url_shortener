from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import get_object_or_404
from .models import ShortURL
from .forms import SubmitUrlForm

class HomeView(View):
    def get(self, request):
        form = SubmitUrlForm()
        template = 'shortener/home.html'
        context = {
            'title': "Submit URL",
            'form': form
        }
        return render(request, template, context)

    def post(self, request):
        template = 'shortener/home.html'
        form = SubmitUrlForm(request.POST)
        context = {
            'title': "Submit URL",
            'form': form
        }
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created
            }
            if created:
                template = "shortener/success.html"
            else:
                template =  "shortener/exists.html"

        return render(request, template, context)

class ShortRedirectView(View):
    def get(self, request, shortcode):
        obj = get_object_or_404(ShortURL, short_code=shortcode)
        return HttpResponseRedirect(obj.url)
