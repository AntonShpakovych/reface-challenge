function deleteNote(notePk) {
    const url = `/notes/${notePk}/delete/`

    fetch(url, {
        method: "DELETE",
        headers: {"X-CSRFToken": csrfToken}
    })
        .then(response => {
            if (response.status === 204) {
                alert("You successfully deleted note!")
                fetchNotes()
            } else {
                alert("You can't do this:)")
            }
        })
}
