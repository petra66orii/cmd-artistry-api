# gallery/admin.py

from django.contrib import admin
from django.utils.html import mark_safe
from .models import GalleryItem

@admin.register(GalleryItem)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_thumbnail', 'created_at')
    list_filter = ('category',)
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        """
        Creates a small thumbnail of the image to display in the admin list.
        """
        if obj.image:
            # Create an HTML img tag with a max width of 100px
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No Image" # Display this text if no image is uploaded
    
    image_thumbnail.short_description = 'Thumbnail' # Sets the column header name