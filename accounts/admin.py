from django.contrib import admin
from .models import Biogram

@admin.register(Biogram)
class BiogramAdmin(admin.ModelAdmin):
    pass
