from django.db import models
from django.utils.html import format_html

# Create your models here.


# Banners
class Banners(models.Model):
    banner_img = models.ImageField(upload_to="banners/")
    alt_text = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Banners"

    def __str__(self):
        return self.alt_text

        # to display image in admin panel

    def image_tag(self):
        return format_html('<img src="{}" width="80" />', self.banner_img.url)


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()
    service_img = models.ImageField(upload_to="services/", null=True)

    def __str__(self):
        return self.title
        # to display image in admin panel

    def image_tag(self):
        return format_html('<img src="{}" width="80" />', self.service_img.url)
    
    #Absolute URL for service detail page
    #TODO: Implement service detail page and uncomment the code below