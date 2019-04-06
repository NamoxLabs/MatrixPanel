from __future__ import unicode_literals

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils import timezone
from django.utils.translation import pgettext_lazy


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False,
                    is_active=True, **extra_fields):
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=is_active,
                        is_staff=is_staff, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user


# user model definition
class User(PermissionsMixin, AbstractBaseUser):
    name = models.CharField(max_length=120, blank=True)
    lastname = models.CharField(max_length=120, blank=True)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    invitation_code = models.CharField(max_length=35, blank=True)
    rol = models.CharField(max_length=25, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = pgettext_lazy('User model', 'user')
        verbose_name_plural = pgettext_lazy('User model', 'users')

    def get_full_name(self):
        return self.email
