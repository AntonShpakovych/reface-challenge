from django import forms
from django.contrib.auth import mixins

from note.models import Note


class UserNotesMixin(mixins.LoginRequiredMixin):
    def get_user_notes(self):
        return Note.objects.select_related("user").filter(
            user=self.request.user
        )

    def get_user_notes_with_category(self):
        return self.get_user_notes().select_related("category")

    def get_user_note_with_category(self, pk):
        return self.get_user_notes().select_related(
            "category"
        ).filter(pk=pk).first()


class BootstrapModalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
