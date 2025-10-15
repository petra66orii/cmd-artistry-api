from django.db import models

# Create your models here.
class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('MURAL', 'Mural'),
        ('POTTERY', 'Pottery'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True, help_text="A short description of the artwork.")
    image = models.ImageField(upload_to='gallery_images/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='MURAL')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Gallery Items"

    def __str__(self):
        return self.title