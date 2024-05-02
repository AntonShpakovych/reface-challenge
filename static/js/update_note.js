function updateNote(pk) {
    const url = `/notes/${pk}/update/`
    const errorsContainer = document.getElementById("form-errors")

    createFormContainer()
    const formContainer = document.getElementById("form-container")
    fillFormContainer(formContainer, url)

    formContainer.addEventListener("submit", (event) => {
        handleFormsSubmission(event, url)

        if (!errorsContainer) {
            setTimeout(() => {
                formContainer.innerHTML = " "
                fillFormContainer(formContainer, url)
            }, 1000)
        }

    })
}
