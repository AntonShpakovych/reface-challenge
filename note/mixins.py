from django.contrib.auth import mixins

from note.models import Note


class UserNotesMixin(mixins.LoginRequiredMixin):
    def get_user_notes(self):
        return Note.objects.select_related("user").filter(
            user=self.request.user
        )


class BootstrapFormClasses:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control form-control-lg"}
            )
