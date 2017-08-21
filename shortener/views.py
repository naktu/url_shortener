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
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, template, {})

class ShortRedirectView(View):
    def get(self, request, shortcode):
        obj = get_object_or_404(ShortURL, short_code=shortcode)
        return HttpResponseRedirect(obj.url)
