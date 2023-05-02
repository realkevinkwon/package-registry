from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page

urlpatterns = [
    # Path to view all files in the bucket
    path('', home_page, name='home_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
