import phonenumbers
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError


from .manager import UserManager

# Create your models here.

def validate_phone(value):
    try:
        x = phonenumbers.parse(value, None)
        if not phonenumbers.is_possible_number(x):
            raise ValidationError(
            "Enter a valid phone number (e.g. +2347012345678) - a number with an international call prefix."
        )
        elif not phonenumbers.is_valid_number(x):
            raise ValidationError(
            "Enter a valid phone number (e.g. +2347012345678) - The number too short or long."
        )
    except phonenumbers.NumberParseException:
        raise ValidationError(
            "Enter a valid phone number (e.g. +2347012345678) - a number with an international call prefix."
        )
class CustomUser(AbstractUser):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female'), ('Male', 'Male'), ('Female', 'Female')]
    username = None
    email = models.EmailField(_('Email address'), unique=True)
    full_name = models.CharField(_("User full name"), max_length=100, blank=True)
    sex = models.CharField(_("User gender"), max_length=6, blank=True, choices=GENDER_CHOICES, default='male')
    phone_number = models.CharField(_("User Phone number"), max_length=20, blank=True, validators=[validate_phone])
    country = models.CharField(_("Country"), blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.email)
