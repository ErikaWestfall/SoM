from django.contrib import admin
from .models import StudentProfile, TeacherProfile, Course, Class, SemesterGrade, Test, Announcement

admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(SemesterGrade)
admin.site.register(Test)
admin.site.register(Announcement)
