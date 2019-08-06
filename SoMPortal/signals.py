from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.dispatch import receiver
from .models import StudentProfile, TeacherProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            profile = TeacherProfile.objects.create(user=instance)
            profile.save()
        elif instance.is_student:
            profile = StudentProfile.objects.create(user=instance)
            profile.save()

