from django.urls import path
from . import views

urlpatterns = [
    path('reset/', views.reset_registry, name='reset_registry'),
    path('reset_form', views.render_reset, name='render_reset'),
    path('reset/success', views.render_reset_success),
]