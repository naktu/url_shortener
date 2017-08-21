from django.db import models
from .utils import create_short_code
from django.conf import settings

SHORT_CODE_MAX = getattr(settings, 'SHORT_CODE_MAX', 15)


class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super().all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_short_codes(self, items=100):
        qs = ShortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.short_code = create_short_code(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class ShortURL(models.Model):
    url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=SHORT_CODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = ShortURLManager()
    some_random = ShortURLManager()

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = create_short_code(self)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
