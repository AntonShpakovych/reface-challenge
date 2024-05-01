from django.http import JsonResponse


def process_forms_validation(note_form, category_form, user, valid_status):
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

    # In the case of an update, I also do this action, for simplicity
    note.user = user
    note.save()

    return JsonResponse(data={}, status=valid_status)
