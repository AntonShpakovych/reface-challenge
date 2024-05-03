from django.contrib.auth import get_user_model
from django.http import JsonResponse
from note.forms import CategoryCreateForm, NoteCreateForm, NoteUpdateForm


User = get_user_model()


def process_forms_validation(
    note_form: NoteCreateForm | NoteUpdateForm,
    category_form: CategoryCreateForm,
    user: User,
    valid_status: int,
    is_create: bool = True
) -> JsonResponse:
    """
    Process validation for note and category forms and save or update data
    """
    if not note_form.is_valid():
        return JsonResponse(
            data={"payload": note_form.errors.as_json()},
            status=400
        )

    note_with_category = note_form.cleaned_data.get("category")

    if note_with_category:
        note = note_form.save(commit=False)
    elif not note_with_category and category_form.is_valid():
        category = category_form.save()
        note = note_form.save(commit=False)
        note.category = category
    else:
        return JsonResponse(
            data={"payload": category_form.errors.as_json()},
            status=400
        )

    if is_create:
        note.user = user
    note.save()

    return JsonResponse(data={}, status=valid_status)
