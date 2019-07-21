from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)   
    birth_date = models.DateField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    role_choices = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher')
    )

    role = models.CharField(
        max_length = 7,
        choices = role_choices
    )

    def __str__(self):
        return f'{self.user.username} Profile'

class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.course_name}'

class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username}'

class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username}'

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    class_code = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)
    teachers = models.ManyToManyField(Teacher)

    def __str__(self):
        return f'{self.class_name}'

class Test(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test_choices = (
        ('Unit 1', 'Unit Test 1'),
        ('Unit 2', 'Unit Test 2'),
        ('Lab 1', 'Lab Test 1'),
        ('Lab 2', 'Lab Test 2'),
        ('Final', 'Final Test'),
    )
    test_type = models.CharField(
        max_length = 10,
        choices = test_choices
    )
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f'{self.student} {self.test_type} score'

class SemesterGrade(models.Model):
    sem_choices = (
        ('1st sem', '1st Semester'),
        ('2nd sem', '2nd Semester'),
        ('3rd sem', '3rd Semester'),
        ('4th sem', '4th Semester'),
        ('5th sem', '5th Semester'),
        ('6th sem', '6th Semester'),
        ('7th sem', '7th Semester'),
        ('8th sem', '8th Semester'),
    )
    semester = models.CharField(
        max_length = 12,
        choices = sem_choices
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    test = models.ManyToManyField(Test)
    
    @property
    def test_score(self):
        return self.test.score

    def __str__(self):
        return f'{self.student.profile.user.username}: {self.semester} Grade'

class Announcement(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        return self.title   
