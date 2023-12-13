import enum

from django.db import models

# 1 sposob
# CATGORIES = (
#     ("vege", "vegetarian"),
#     ("meat", "meat"),
#     ("fish", "fish"),
#     ("fruit", "fruit")
# )

# 2 sposob
# class Categories(enum.Enum):
#     VEGE = "vege"
#     MEAT = "meat"
#
#     @classmethod
#     def choices(cls):
#         return [(item.value, item.name) for item in cls]


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        "recipes.Category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="recipes",
    )
    tags = models.ManyToManyField("tags.Tag", related_name="recipes")

    def __str__(self):
        return f"{self.id}: {self.title}"
