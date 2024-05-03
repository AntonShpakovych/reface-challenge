function getNotes() {
    const noteContainer = document.getElementById("note-container")
    let url = "/notes/" + "?" + globalQueryParams.toString()

    fetch(url, {
        method: "GET",
    })
        .then(response => {
            if (response.status === 200) {
                return response.json()
            } else {
                throw new Error("Not found")
            }
        })
        .then(data => {
            noteContainer.innerHTML = ""

            handlePagination(data.payload.paginator)

            data.payload.paginator.notes.forEach(note => {
                let noteHtml = generateNoteHtml(note)
                noteContainer.innerHTML += noteHtml
            })
        })
        .catch(error => {
            noteContainer.innerHTML = "<h1>With these filters, you don't have notes, or you don't have any at all</h1>"
        });
}

addEventListener("DOMContentLoaded", (event) => {
    const timeForLookingDbUpdates = 60 * 1000
    // Initial FETCH
    getNotes()
    // Looking for db updates
    setInterval(getNotes, timeForLookingDbUpdates);
});
