import json

from django.contrib.auth import mixins
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


from note.forms import NoteCreateForm, NoteUpdateForm, CategoryCreateForm
from note.mixins import UserNotesMixin

from note.utils.process_forms_validation import process_forms_validation
from note.utils import statuses


class IndexView(mixins.LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "note/note_list.html")


class NoteListView(UserNotesMixin, View):
    def get(self, request):
        notes = self.get_user_notes_with_category().values(
            "pk",
            "text",
            "status",
            "user",
            category_color=F("category__color")
        )

        if notes:
            return JsonResponse(
                data={"payload": json.dumps(list(notes))},
                status=statuses.HTTP_200_OK
            )
        return JsonResponse(data={}, status=statuses.HTTP_404_NOT_FOUND)


class DeleteNoteView(UserNotesMixin, View):
    def delete(self, request, pk):
        note = self.get_user_notes().filter(pk=pk).first()

        if note:
            note.delete()

            return JsonResponse(data={}, status=statuses.HTTP_204_NO_CONTENT)
        return JsonResponse(data={}, status=statuses.HTTP_404_NOT_FOUND)


class DetailNoteView(UserNotesMixin, View):
    def get(self, request, pk):
        note = self.get_user_notes_with_category().values(
            "text",
            "status",
            "created_at",
            category_name=F("category__name")
        ).filter(pk=pk).first()

        if note:
            note["created_at"] = str(note["created_at"])
            payload = json.dumps(note)
            return JsonResponse(
                data={"payload": payload},
                status=statuses.HTTP_200_OK
            )
        return JsonResponse(data={}, status=statuses.HTTP_404_NOT_FOUND)


class CreateNoteView(View):
    def get(self, request):
        note_form = NoteCreateForm()
        category_form = CategoryCreateForm()

        return JsonResponse(
            data={
                "payload": {
                    "note_form": note_form.as_p(),
                    "category_form": category_form.as_p()
                }
            },
            status=statuses.HTTP_200_OK
        )

    def post(self, request):
        note_form = NoteCreateForm(request.POST)
        category_form = CategoryCreateForm(request.POST)

        return process_forms_validation(
            note_form=note_form,
            category_form=category_form,
            user=request.user,
            valid_status=statuses.HTTP_201_CREATED
        )


class UpdateNoteView(UserNotesMixin, View):
    def get(self, request, pk):
        note = self.get_user_note_with_category(pk=pk)

        if note:
            note_form = NoteUpdateForm(instance=note)
            category_form = CategoryCreateForm()

            return JsonResponse(
                data={
                    "payload": {
                        "note_form": note_form.as_p(),
                        "category_form": category_form.as_p()
                    }
                },
                status=statuses.HTTP_200_OK
            )

        return JsonResponse(data={}, status=statuses.HTTP_404_NOT_FOUND)

    def post(self, request, pk):
        note = self.get_user_note_with_category(pk=pk)
        note_form = NoteUpdateForm(request.POST, instance=note)
        category_form = CategoryCreateForm(request.POST)

        return process_forms_validation(
            note_form=note_form,
            category_form=category_form,
            user=request.user,
            valid_status=statuses.HTTP_200_OK
        )
