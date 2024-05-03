from django.contrib.auth.models import AbstractUser
from django.db import models

from user.manager import UserManager
from user.utils import validators


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)
    password = models.CharField(
        validators=[
            validators.password_validator
        ]
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ["email"]
