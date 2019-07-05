from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("Users must have a username.")
        if not password:
            raise ValueError("Users must have a password.")
        if not email:
            raise ValueError("Users must have an email address.")
        if not first_name:
            raise ValueError("Users must have a first name address.")
        if not last_name:
            raise ValueError("Users must have a last name address.")
        user_obj = self.model(
            username = username,
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.save(self._db)
        return user_obj

    def create_staffuser(self, username, email, first_name, last_name, password):
        user = self.create_user(
            username,        
            email,
            first_name,
            last_name,
            password = password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None):
        user = self.create_user(
            username,        
            email,
            first_name,
            last_name,
            password = password,
            is_staff=True,
            is_admin=True,
        )
        return user

class User(AbstractBaseUser):
    username = models.CharField(
        max_length = 150,
        unique = True,
    )
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user an admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active