from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db import models

from note.utils import messages


User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=15
    )
    color = models.CharField(
        validators=[RegexValidator(
            regex=r"^#[0-9A-F]{6}$",
            message=messages.CATEGORY_COLOR_VALIDATION,
            code="invalid_color"
        )],
        max_length=7
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
        unique_together = ["name", "color"]
        verbose_name_plural = "Categories"


class Note(models.Model):
    class NoteStatusChoices(models.TextChoices):
        ACTIVE = "Active", _("Active")
        ARCHIVED = "Archived", _("Archived")

    text = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="notes",
    )
    status = models.CharField(
        choices=NoteStatusChoices.choices,
        default=NoteStatusChoices.ACTIVE,
        max_length=8
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
