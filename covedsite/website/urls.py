from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('mentor/', views.mentor, name='mentor'),
    path('student/', views.student, name='student'),
    path('resources/', views.aboutUs, name='resources'),
]