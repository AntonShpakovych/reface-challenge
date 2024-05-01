from django.urls import path

from note import views


urlpatterns = [
    path("page/", views.IndexView.as_view(), name="index"),
    # JS views
    path(
        "",
        views.NoteListView.as_view(),
        name="note-list"
    ),
    path(
        "create/",
        views.CreateNoteView.as_view(),
        name="create-note"
    ),
    path(
        "<int:pk>/delete/",
        views.DeleteNoteView.as_view(),
        name="delete-note"
    ),
    path(
        "<int:pk>/detail/",
        views.DetailNoteView.as_view(),
        name="detail-note"
    ),
    path(
        "<int:pk>/update/",
        views.UpdateNoteView.as_view(),
        name="update-note"
    )
]

app_name = "note"
