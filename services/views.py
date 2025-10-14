from rest_framework import generics
from .models import Service
from .serializers import ServiceSerializer

# This view handles listing all services
class ServiceList(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# This view handles retrieving a single service by its slug
class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug' # Important: this tells the view to find the service by its slug