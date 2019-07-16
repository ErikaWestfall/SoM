from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='user-profile'),
    path('announcements/', views.Announcements, name='SoM-announcements'),
    path('events/', views.Events, name='SoM-events'),
    path('forum/', views.Forum, name='SoM-forum'),
]