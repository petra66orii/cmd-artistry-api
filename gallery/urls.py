from django.urls import path
from .views import GalleryItemList

urlpatterns = [
    path('', GalleryItemList.as_view(), name='gallery-item-list'),
    ]