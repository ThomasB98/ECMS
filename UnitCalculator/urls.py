from django.urls import path
from . import views

urlpatterns = [
    path('sudobill', views.device_form_view, name='sudobill'),
]
