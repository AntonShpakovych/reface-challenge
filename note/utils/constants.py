CATEGORY_NAME_MAX_LENGTH = 15
CATEGORY_COLOR_MAX_LENGTH = 7
CATEGORY_COLOR_PATTERN = r"^#[0-9A-F]{6}$"
CATEGORY_COLOR_CODE = "invalid_color"

NOTE_STATUS_MAX_LENGTH = 8
NODE_STATUS_ACTIVE_DB = "Active"
NODE_STATUS_ARCHIVED_DB = "Archived"

NOTE_SORT_CHOICES_FORM = (
    ("created_at", "Date"),
    ("word_count", "Word Count"),
    ("unique_word_count", "Unique Word Count"),
    ("category", "Category")
)

NOTES_PAGINATED_BY = 9
