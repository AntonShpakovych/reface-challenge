from django.contrib.auth.models import AbstractUser
from django.db import models

from user.manager import UserManager
from user.utils import validators, constants


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    password = models.CharField(
        max_length=constants.PASSWORD_MAX_LENGTH,
        validators=[validators.password_validator]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["email"]
