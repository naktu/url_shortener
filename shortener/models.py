from django.db import models


class ShortURL(models.Model):
    url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.url)
