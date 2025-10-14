from django.urls import path
from .views import TestimonialList

urlpatterns = [
    path('testimonials/', TestimonialList.as_view(), name='testimonial-list'),
]