from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "short_description"]

    @staticmethod
    def short_description(obj):
        return obj.description[:15] + "..."

    def get_list_display(self, request):
        """Overwriting method responsible for displaying list of objects"""
        if request.user.is_superuser:
            return self.list_display
        return ["title"]

