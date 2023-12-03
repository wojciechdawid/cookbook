from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.title}"
