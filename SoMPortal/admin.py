from django.contrib import admin
from .models import Profile, Course, Student, Teacher, Class, SemesterGrade, Test, Announcement

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(SemesterGrade)
admin.site.register(Test)
admin.site.register(Announcement)
