import json

from django.shortcuts import render
from django.contrib.auth import mixins
from django.http import JsonResponse, HttpRequest
from django.db.models import F
from django.views import View


from note.forms import (
    NoteCreateForm,
    NoteUpdateForm,
    CategoryCreateForm,
)
from note.mixins import UserNotesMixin
from note.models import Note
from note.utils.note_filter_sort_service import NoteFilterSortService
from note.utils.pagination_service import NotePaginationService

from note.utils.process_forms_validation import process_forms_validation
from note.utils import statuses


class IndexView(mixins.LoginRequiredMixin, View):
    """
    A view class for rendering the index page.
    """
    def get(self, request):
        return render(request, "note/page.html")


class NoteListView(UserNotesMixin, View):
    """
    A view class for listing notes associated with the current user.
    """
    paginated_by = 3

    def get(self, request: HttpRequest) -> JsonResponse:
        notes = NoteFilterSortService(
            base_query=self.get_user_notes().select_related("category"),
            filter=request.GET.get("filter_by"),
            sort=request.GET.get("sort_by")
        ).handle_querying().values(
            "pk",
            "text",
            "status",
            category_color=F("category__color")
        )

        paginator = NotePaginationService(notes, self.paginated_by)

        if notes:
            return JsonResponse(
                data={
                    "payload": {
                        "paginator": paginator.split_data_for_js(
                            request.GET.get("page")
                        )
                    }
                },
                status=statuses.HTTP_200_OK
            )
        return JsonResponse(data={}, status=statuses.HTTP_404_NOT_FOUND)


class DeleteNoteView(UserNotesMixin, View):
    """
    A view class for deleting a note associated with the current user.
    """
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        note = self.get_user_notes().filter(pk=pk).first()

        if note:
            note.delete()

            return JsonResponse(data={}, status=statuses.HTTP_204_NO_CONTENT)
        return JsonResponse(data={}, status=statuses.HTTP_404_NOT_FOUND)


class DetailNoteView(UserNotesMixin, View):
    """
    A view class for retrieving details of a note
    associated with the current user.
    """
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        note = self.get_user_notes().select_related(
            "category"
        ).values(
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
    """
    A view class for creating a new note
    """
    def get(self, request: HttpRequest) -> JsonResponse:
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

    def post(self, request: HttpRequest) -> JsonResponse:
        note_form = NoteCreateForm(request.POST)
        category_form = CategoryCreateForm(request.POST)

        return process_forms_validation(
            note_form=note_form,
            category_form=category_form,
            user=request.user,
            valid_status=statuses.HTTP_201_CREATED
        )


class UpdateNoteView(UserNotesMixin, View):
    """
    A view class for updating an existing note
    associated with the current user.
    """
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        note = self.get_object(pk=pk)

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

    def post(self, request: HttpRequest, pk: int) -> JsonResponse:
        note = self.get_object(pk=pk)
        note_form = NoteUpdateForm(request.POST, instance=note)
        category_form = CategoryCreateForm(request.POST)

        return process_forms_validation(
            note_form=note_form,
            category_form=category_form,
            user=request.user,
            valid_status=statuses.HTTP_200_OK,
            is_create=False
        )

    def get_object(self, pk: int) -> Note | None:
        return self.get_user_notes().select_related(
            "category"
        ).filter(pk=pk).first()
