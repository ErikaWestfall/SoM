from django.conf import settings
from django.db import models

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


