from django.db import models

class Hero (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self) -> str:
        return super().__str__(f'Name {self.name}')