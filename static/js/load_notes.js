function getNotes(){

    const noteContainer = document.getElementById("note-container")
    const noteFilterSortForm = document.getElementById("note-filter-sort-form")
    const formData =  new FormData(noteFilterSortForm)
    const queryParams = new URLSearchParams(formData).toString();
    let url = "/notes/" + "?" + queryParams

    fetch(url, {
        method: "GET",
    })
        .then(response => {
            if (response.status === 200){
                return response.json()
            } else{
                throw new Error("Not found")
            }
        })
        .then(data => {
            noteContainer.innerHTML = ""

            JSON.parse(data.payload.notes).forEach(note =>{
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
