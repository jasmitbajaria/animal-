from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    path('', include('home.urls')),  # Include URLs from the 'home' app (make sure 'home.urls' exists)
    
]

# This will ensure media files are served during development
if settings.DEBUG:  # Only include this in development (DEBUG mode is True)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

