from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db import models

from note.utils import constants, messages


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
        return f"<Category: {self.id}>"

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
        on_delete=models.SET_NULL,
        related_name="notes",
        null=True,
        blank=True
    )
    status = models.CharField(
        choices=NoteStatusChoices.choices,
        default=NoteStatusChoices.ACTIVE,
        max_length=constants.NOTE_STATUS_MAX_LENGTH
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"<Note: id={self.id}>"

    class Meta:
        ordering = ["created_at"]
