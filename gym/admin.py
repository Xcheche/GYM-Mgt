from django.contrib import admin
from .models import Banners, Service

# Register your models here.


class BannersAdmin(admin.ModelAdmin):
    list_display = ["alt_text", "image_tag"]
    list_display_links = ["alt_text", "image_tag"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag"]
    list_display_links = ["title", "image_tag"]


admin.site.register(Banners, BannersAdmin)
admin.site.register(Service, ServiceAdmin)
