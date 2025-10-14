from django.db import models
class Testimonial(models.Model):
    """Represents a testimonial from a client."""
    quote = models.TextField()
    author_name = models.CharField(max_length=100)
    company_or_title = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="e.g., 'Homeowner' or 'CEO of Cafe Name'"
    )
    is_approved = models.BooleanField(
        default=False, 
        help_text="Only approved testimonials will be shown on the site."
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'"{self.quote[:30]}..." by {self.author_name}'


class NewsletterSubscriber(models.Model):
    """Stores email addresses for the newsletter."""
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email