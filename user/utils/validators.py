import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from user.utils import messages


def password_validator(value: str) -> None:
    """
    Validate the password value against certain criteria.
    """
    min_length = 8

    pattern = fr"^(?=.*?[A-Z])" \
              fr"(?=.*?[a-z])" \
              fr"(?=.*?[0-9])" \
              fr"(?=.*?[#?!@$%^&*-])" \
              fr".{{{min_length},}}$"

    if not re.match(pattern, value):
        raise ValidationError(
            _(messages.USER_PASSWORD_VALIDATION),
            code="invalid_password",
        )


class AdminPasswordValidator:
    """
    A password validator for administrative users.
    """
    def validate(self, password: str, user=None) -> None:
        password_validator(password)

    def get_help_text(self) -> str:
        return _(messages.USER_PASSWORD_VALIDATION)
