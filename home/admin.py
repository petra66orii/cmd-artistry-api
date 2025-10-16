from django.contrib import admin
from .models import Testimonial, NewsletterSubscriber

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    Customizes the admin view for Testimonials.
    """
    list_display = ('author_name', 'quote_preview', 'is_approved', 'submitted_at')
    list_filter = ('is_approved',)
    # This allows approving testimonials directly from the list view
    list_editable = ('is_approved',)
    search_fields = ('author_name', 'quote')

    def quote_preview(self, obj):
        # Returns the first 50 characters of the quote for a clean list view
        return f'"{obj.quote[:50]}..."'
    quote_preview.short_description = 'Quote'


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    """
    Customizes the admin view for Newsletter Subscribers.
    """
    list_display = ('email', 'subscribed_at')
    readonly_fields = ('subscribed_at',)
    search_fields = ('email',)