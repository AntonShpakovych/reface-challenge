function createFormAlertContainer(id, className) {
    const container = document.createElement("div")
    container.id = id
    container.className = className
    container.role = "alert"
    return container
}

function createFormContainer(){
    const formContainer = document.createElement("form")

    formContainer.id = "form-container"
    formContainer.noValidate = true

    const errorsContainer = createFormAlertContainer(
        "form-errors",
        "alert alert-danger d-none"
    );
    const successContainer = createFormAlertContainer(
        "form-success",
        "alert alert-success d-none"
    );

    modalBodyContainer.appendChild(successContainer)
    modalBodyContainer.appendChild(errorsContainer)
    modalBodyContainer.appendChild(formContainer)

}


function fillFormContainer(formContainer, url) {
    fetch(url, {
        method: "GET"
    })
        .then(response => response.json())
        .then(data => {
            const { note_form, category_form } = data.payload;
            const submitButton = '<button id="submit-note-form" class="btn btn-success">Submit</button>';
            const helpText = "<p>Or you can create a new Category:</p>";

            formContainer.innerHTML = `${note_form}${helpText}${category_form}${submitButton}`;
        })
}


function handleFormsSubmission(event, url) {
    event.preventDefault()

    const noteAndCategoryFormData = new FormData(event.target)

    fetch(url, {
        method: "POST",
        headers: {"X-CSRFToken": csrfToken},
        body: noteAndCategoryFormData,
    })
        .then(response => {
            return Promise.all([response.status, response.json()])
        })
        .then(([status, data]) => {
            if (status === 201 || status === 200){
                const statusMessage = status === 201 ? "created" : "updated"
                handleUserNotification(statusMessage)
            } else {
                handleUserNotification(null, false, data.payload);
            }
        })
}

function handleHtmlErrors(errors) {
    const errorsToObject = JSON.parse(errors)
    let html = ""

    for (const field in errorsToObject) {
        const message = errorsToObject[field][0]["message"]
        html += `<ul><li>${field}<ul><li>${message}</li></ul></li></ul>`;
    }
    return html
}

function handleUserNotification(status= null, isValid = true, data = null) {
    const successContainer = document.getElementById("form-success");
    const errorsContainer = document.getElementById("form-errors");

    if (isValid) {
        errorsContainer.classList.add("d-none")
        successContainer.innerHTML = `Note successfully ${status}! You can close this window or add new :`;
        successContainer.classList.remove("d-none");


        setTimeout(() => {
            successContainer.innerHTML = "";
            successContainer.classList.add("d-none");
        }, 3000);
    } else {
        errorsContainer.innerHTML = handleHtmlErrors(data);
        errorsContainer.classList.remove("d-none");
    }
}


function generateNoteHtml(note) {
    return `
    <div id="note-${note.pk}" class="col-lg-4 col-md-6 col-sm-12 mb-4">
      <div style="box-shadow: 0 0 10px 1px ${note.category_color}" class="card card h-100 d-flex flex-column">
        <div class="card-title">
            <div id="card-title-status">status: ${note.status}</div>
        </div>
        <hr>
        <div class="card-body">
            <div class="text-muted description"><small>text: </small>${note.text.slice(0,20)}...</div>
            <div class="d-flex align-items-center justify-content-between pt-3">
                <button onclick="getNote(${note.pk})" type="button" class="detail-note btn btn-primary" data-toggle="modal" data-target="#note-modal-container">
                    Detail
                </button>
                <button onclick="updateNote(${note.pk})" type="button" class="detail-note btn btn-primary" data-toggle="modal" data-target="#note-modal-container">
                    Update
                </button>
                <button onclick="deleteNote(${note.pk})" type="button" class="delete-note btn btn-danger">Delete
                </button>
            </div>
        </div>
      </div>
    </div>`
}

function fetchNotes() {
    setTimeout(getNotes, 500)
}
