from django import forms

from note.models import Note, Category
from note import mixins
from note.utils.constants import NOTE_SORT_CHOICES_FORM
from note.utils import messages


class NoteCreateForm(mixins.BootstrapFormClasses, forms.ModelForm):
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


class CategoryCreateForm(mixins.BootstrapFormClasses, forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "color"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": messages.CATEGORY_NAME_PLACEHOLDER}
            ),
            "color": forms.TextInput(
                attrs={"placeholder": messages.CATEGORY_COLOR_PLACEHOLDER}
            )
        }


class NoteFilterSorterForm(mixins.BootstrapFormClasses, forms.Form):
    sort_by = forms.ChoiceField(
        label="Sort by",
        choices=NOTE_SORT_CHOICES_FORM,
        required=False,
    )
    filter_by = forms.ChoiceField(
        label="Filter by",
        choices=Note.NoteStatusChoices.choices,
        required=False,
    )
