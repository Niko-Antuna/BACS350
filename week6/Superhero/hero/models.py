from django.db import models
from django.urls.base import reverse_lazy


class Hero (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - Description: {self.description}'

    def get_absolute_url(self):
        return reverse_lazy('hero_list')
