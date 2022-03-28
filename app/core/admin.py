from django.contrib import admin

from core.models import URL

# Register your models here.

@admin.register(URL)
class URLModelAdmin(admin.ModelAdmin):
    pass