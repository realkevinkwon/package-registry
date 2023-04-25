from django.urls import path
from .views import restart_registry

urlpatterns = [
    # Path to restart all files in the bucket
    path('restart', restart_registry, name='restart_registry'),
]