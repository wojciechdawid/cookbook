from django.core.validators import RegexValidator
from django.db import models


class Problem(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=15, validators=[
        RegexValidator(
            regex="\d{9}",
            message="Bad phone number"
        )
    ])
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
