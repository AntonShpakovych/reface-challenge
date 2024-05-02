from note.forms import NoteFilterSorterForm


def get_note_filter_sorter_form(request):
    return {"note_filter_sorter_form": NoteFilterSorterForm()}
