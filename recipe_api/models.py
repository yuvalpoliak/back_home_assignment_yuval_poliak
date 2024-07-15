from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    hot = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    def __str__(self):
        return self.title