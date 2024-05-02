from typing import re

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db import models

from note.utils import constants, messages


User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=constants.CATEGORY_NAME_MAX_LENGTH
    )
    color = models.CharField(
        validators=[RegexValidator(
            regex=constants.CATEGORY_COLOR_PATTERN,
            message=messages.CATEGORY_COLOR_VALIDATION,
            code=constants.CATEGORY_COLOR_CODE
        )],
        max_length=constants.CATEGORY_COLOR_MAX_LENGTH
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"


class Note(models.Model):
    class NoteStatusChoices(models.TextChoices):
        ACTIVE = constants.NODE_STATUS_ACTIVE_DB, _("Active")
        ARCHIVED = constants.NODE_STATUS_ARCHIVED_DB, _("Archived")

    text = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    status = models.CharField(
        choices=NoteStatusChoices.choices,
        default=NoteStatusChoices.ACTIVE,
        max_length=constants.NOTE_STATUS_MAX_LENGTH
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notes"
    )

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        ordering = ["-created_at"]
