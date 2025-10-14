from django.db import models

class Service(models.Model):
    """Represents a service offered by the artist, e.g., Mural Painting."""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, help_text="A unique URL-friendly version of the title.")
    summary = models.TextField(help_text="A short summary for the services overview page.")
    detailed_description = models.TextField(help_text="The full description for the service's dedicated page.")
    image = models.ImageField(upload_to='service_images/', blank=True, null=True, help_text="An image representing the service.")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title