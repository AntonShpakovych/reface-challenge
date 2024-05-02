from note.forms import NoteFilterSorterForm


def get_note_filter_sort_form(request):
    return {"note_filter_sort_form": NoteFilterSorterForm()}
