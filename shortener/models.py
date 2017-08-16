from django.db import models
from .utils import create_shortcode


class ShortURL(models.Model):
    url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == "":
            self.short_code = create_shortcode(self)
            super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
