from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import permission_denied_view
from contact.views import get_csrf_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/services/', include('services.urls')),
    path('api/contact/', include('contact.urls')),
    path('api/home/', include('home.urls')),
    path('api/gallery/', include('gallery.urls')),
    path('api/get-csrf-token/', get_csrf_token, name='get-csrf-token'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = permission_denied_view