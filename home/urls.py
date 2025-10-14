from django.urls import path
from .views import TestimonialList, NewsletterSubscribe

urlpatterns = [
    path('testimonials/', TestimonialList.as_view(), name='testimonial-list'),
    path('newsletter/subscribe/', NewsletterSubscribe.as_view(), name='newsletter-subscribe'),
]