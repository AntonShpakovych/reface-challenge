setInterval(getNotes, 1000)

function getNotes(){
    const url = "/notes"
    const noteContainer = document.getElementById("note-container")

    fetch(url, {
        method: "GET"
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
            JSON.parse(data.payload).forEach(note =>{
                let noteHtml = generateNoteHtml(note)
                noteContainer.innerHTML += noteHtml
            })
        })
        .catch(error => {
            noteContainer.innerHTML = "<h1>With these filters, you don't have notes, or you don't have any at all</h1>"
        });
}
