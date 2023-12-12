from django.db import models


class Biogram(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateTimeField()
    death_date = models.DateTimeField(null=True, blank=True)

    def is_living(self):
        return self.death_date is None
