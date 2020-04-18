from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('mentor/', views.mentor, name='mentor'),
    path('student/', views.student, name='student'),
    path('resources/', views.resources, name='resources'),
    path('studentSignUp/', views.studentSignUp, name='studentsignup'),
    path('mentorSignUp/', views.mentorSignUp, name='mentorsignup'),
    path('resForm/', views.resForm, name='resform'),
]