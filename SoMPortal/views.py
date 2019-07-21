from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Announcement

@login_required
def profile(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': f'{user}'}

    return render(request, 'SoMPortal/profile.html', context)

@login_required
def Announcements(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': 'Announcements', 'Announcements': Announcement.objects.all()}

    return render(request, 'SoMPortal/Announcements.html', context)

@login_required
def Events(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': 'Events'}

    return render(request, 'SoMPortal/events.html', context)

@login_required
def Forum(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user

    context = {'user': user, 'title': 'Forum'}

    return render(request, 'SoMPortal/forum.html', context)
