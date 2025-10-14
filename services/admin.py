from django.contrib import admin
from .models import Service

# This customizes how the Service model appears in the admin
class ServiceAdmin(admin.ModelAdmin):
    # This shows the title and slug in the list view of services
    list_display = ('title', 'slug')
    
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)