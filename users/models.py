
from django.db import models

from django.contrib.auth.models import AbstractUser,UserManager
from django.utils.translation import ugettext_lazy as _



class CutomUserManger(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """

        email = self.normalize_email(email)
        #username = self.model.normalize_username(username)
        user = self.model( email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)


class Users(AbstractUser):

    username = None
    email = models.EmailField(_('email address'), unique=True,blank=False,null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CutomUserManger()

    def __str__(self):
        return self.email


