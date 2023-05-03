from django.urls import path
from . import views

urlpatterns = [
    path('authenticate', views.auth_func, name='authentication'),
]