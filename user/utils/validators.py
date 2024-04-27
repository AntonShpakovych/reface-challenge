import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from user.utils import messages, constants


def password_validator(value):
    min_length = constants.PASSWORD_MIN_LENGTH

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
    def validate(self, password, user=None):
        password_validator(password)

    def get_help_text(self):
        return _(messages.USER_PASSWORD_VALIDATION)
