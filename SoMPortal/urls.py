from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
    path('announcements/', views.Announcements, name='SoM-announcements'),
    path('events/', views.Events, name='SoM-events'),
    path('forum/', views.Forum, name='SoM-forum'),
    path('grades/', views.grades, name='SoM-grades'),
    path('classes/', views.classes, name='SoM-classes'),
    path('cashier/', views.Cashier, name='SoM-cashier'),
    path('mystudents/', views.myStudents, name='SoM-myStudents'),
]