from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', '남자'),
        ('F', '여자'),
    )

    nickname = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=10, null=False, blank=False)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    birthday = models.DateField(null=False, blank=False)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    produce_me = models.TextField(null=True, blank=True)

    followings = models.ManyToManyField(
        'self', symmetrical=False, related_name="followers", blank=True)
    
