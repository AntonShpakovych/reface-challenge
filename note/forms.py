from django import forms

from note.models import Note, Category
from note import mixins


class NoteCreateForm(mixins.BootstrapModalForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select an category",
        required=False
    )

    class Meta:
        model = Note
        fields = ["text", "category"]


class NoteUpdateForm(NoteCreateForm):
    class Meta(NoteCreateForm.Meta):
        fields = NoteCreateForm.Meta.fields + ["status"]


class CategoryCreateForm(mixins.BootstrapModalForm):
    class Meta:
        model = Category
        fields = ["name", "color"]
