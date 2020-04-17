from django.urls import path
from . import views

urlpatterns = [
    path('aboutUs/', views.aboutUs, name='aboutUs'),
]