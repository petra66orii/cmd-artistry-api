from django.urls import path
from .views import ServiceList, ServiceDetail

urlpatterns = [
    # URL for the list of services: e.g., /api/services/
    path('', ServiceList.as_view(), name='service-list'),
    # URL for a single service detail: e.g., /api/services/mural-painting/
    path('<slug:slug>/', ServiceDetail.as_view(), name='service-detail'),
]