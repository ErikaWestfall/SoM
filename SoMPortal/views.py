from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *

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

@login_required
def grades(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user
    context = {'user': user, 'title': 'Grades'}

    return render(request, 'SoMPortal/grades.html', context)

@login_required
def classes(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user
    context = {'user': user, 'title': 'Classes', 'classes': user.studentprofile.class_set.all()}

    return render(request, 'SoMPortal/classes.html', context)

@login_required
def Cashier(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user
    context = {'user': user, 'title': 'Cashier'}

    return render(request, 'SoMPortal/cashier.html', context)

@login_required
def myStudents(request, username=None):
    if username:
        user = settings.AUTH_USER_MODEL.objects.get(username=username)
    else:
        user = request.user
    context = {'user': user, 'title': 'Cashier', 'classes': user.teacherprofile.class_set.all()}

    return render(request, 'SoMPortal/myStudents.html', context)
