from django.contrib.auth import mixins
from django.db.models import QuerySet

from note.models import Note


class UserNotesMixin(mixins.LoginRequiredMixin):
    """
    A mixin for retrieving notes associated with the current user.
    """
    def get_user_notes(self) -> QuerySet:
        return Note.objects.select_related("user").filter(
            user=self.request.user
        )


class BootstrapFormClasses:
    """
    A mixin class to add Bootstrap form classes to form fields.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control form-control-lg"}
            )
