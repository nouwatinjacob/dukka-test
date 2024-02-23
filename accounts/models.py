from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

from .manager import UserManager

# Create your models here.
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('Email address'), unique=True)
    full_name = models.CharField(_("User full name"), max_length=100, blank=True)
    sex = models.CharField(_("User gender"), max_length=6, blank=True)
    phone_number = models.CharField(_("User Phone number"), max_length=20, blank=True)
    country = CountryField(_("Country"), blank=True, default='NG')
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.email)