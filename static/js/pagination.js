function updatePage(page) {
    globalQueryParams.set("page", page.toString());
    fetchNotes();
}


function handlePagination(paginator) {
    const paginationContainer = document.getElementById("pagination-container");
    const buttonNext = paginationContainer.querySelector(".pagination #pagination-next");
    const buttonPrev = paginationContainer.querySelector(".pagination #pagination-prev");
    const currentPage = parseInt(paginator.current_page)

    globalQueryParams.set("page", currentPage)

    paginationContainer.style.display = (paginator.has_previous || paginator.has_next) ? "flex" : "none";
    buttonPrev.style.display = paginator.has_previous ? "inline" : "none";
    buttonNext.style.display = paginator.has_next ? "inline" : "none";



    buttonPrev.onclick = () => updatePage(currentPage - 1);
    buttonNext.onclick = () => updatePage(currentPage + 1);
}
