from note.db_functions import CountWords, CountUniqueWords


class NoteFilterSortService:
    AVAILABLE_FILTERS = ["Active", "Archived"]
    AVAILABLE_SORTS = {
        "created_at": lambda base_query: base_query.order_by("-created_at"),
        "word_count": lambda base_query: base_query.annotate(
            count_word=CountWords("text")
        ).order_by("-count_word"),
        "category": lambda base_query: base_query.order_by("category"),
        "unique_word_count": lambda base_query: base_query.annotate(
            count_unique_words=CountUniqueWords("text")
        ).order_by("-count_unique_words")
    }

    def __init__(self, filter, sort, base_query):
        self.filter = filter
        self.sort = sort
        self.base_query = base_query

    def handle_querying(self):
        query = self.base_query

        if self.filter in self.AVAILABLE_FILTERS:
            query = query.filter(status=self.filter)
        if self.sort in self.AVAILABLE_SORTS:
            query = self.AVAILABLE_SORTS[self.sort](query)
        return query
