from django.contrib import admin
from .models import GalleryItem

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',) # This adds the filter sidebar

admin.site.register(GalleryItem, GalleryAdmin)