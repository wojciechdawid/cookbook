from django.contrib import admin

from .models import Problem

# Register your models here.
@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    pass