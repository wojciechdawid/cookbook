from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    readonly_fields = ["author", "title", "content"]

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        if request.user == obj.author:
            return ["author"]
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not obj.author:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)


