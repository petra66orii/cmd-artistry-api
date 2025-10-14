from rest_framework import generics
from .models import Testimonial
from .serializers import TestimonialSerializer

class TestimonialList(generics.ListAPIView):
    """
    Provides a list of approved testimonials.
    """
    serializer_class = TestimonialSerializer
    
    def get_queryset(self):
        # This is the key part: only return testimonials where is_approved is True
        return Testimonial.objects.filter(is_approved=True)