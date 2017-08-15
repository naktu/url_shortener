from django.db import models

class ShortURL(models.Model):
    url = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.url)