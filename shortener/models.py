import random

from string import ascii_letters, digits
from django.db import models

def code_generator(size=7, chars=ascii_letters+digits):
    return ''.join(random.choice(chars) for _ in range(size))

class ShortURL(models.Model):
    url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.short_code = code_generator()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
