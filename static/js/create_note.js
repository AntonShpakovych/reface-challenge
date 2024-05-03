function createNote(){
    const url = "/notes/create/"

    createFormContainer()
    const formContainer = document.getElementById("form-container")
    fillFormContainer(formContainer, url)

    formContainer.addEventListener("submit", (event)=>{
        handleFormsSubmission(event, url)
        fetchNotes()
    })
}
