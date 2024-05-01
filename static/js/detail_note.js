function getNote(notePk){
    const url = `/notes/${notePk}/detail/`

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
            const { category_name, status, text, created_at: createdAt } = JSON.parse(data["payload"]);

            modalBodyContainer.innerHTML += `<h6>Category: ${category_name}</h6>`
            modalBodyContainer.innerHTML += `<h6>Status: ${status}</h6>`
            modalBodyContainer.innerHTML += `<h6>Created at: ${new Date(createdAt).toLocaleString("uk-UA")}</h6>`
            modalBodyContainer.innerHTML += `<p>Text: ${text}</p>`
        })
        .catch(error => {
            modalBodyContainer.innerHTML += `<h6>You can't do this:)</h6>`
        })
}
