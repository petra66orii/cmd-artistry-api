from rest_framework import generics
from .models import Testimonial, NewsletterSubscriber
from .serializers import TestimonialSerializer, NewsletterSubscriberSerializer
from rest_framework.response import Response
from rest_framework import status

class TestimonialList(generics.ListAPIView):
    """
    Provides a list of approved testimonials.
    """
    serializer_class = TestimonialSerializer
    
    def get_queryset(self):
        # This is the key part: only return testimonials where is_approved is True
        return Testimonial.objects.filter(is_approved=True)


class TestimonialList(generics.ListAPIView):
    # ... your existing TestimonialList view ...
    pass

# --- Add this new view ---
class NewsletterSubscribe(generics.CreateAPIView):
    """
    Handles new newsletter subscriptions.
    """
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer

    def create(self, request, *args, **kwargs):
        # This customization handles cases where an email already exists
        try:
            return super().create(request, *args, **kwargs)
        except Exception:
             # If the email is a duplicate (unique=True), it will throw an exception.
            return Response(
                {"error": "This email address is already subscribed."},
                status=status.HTTP_400_BAD_REQUEST
            )