from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class NotePaginationService(Paginator):
    """
    A service class for paginating notes data.
    """
    def split_data_for_js(self, page_number: str) -> dict:
        page = None

        try:
            page = self.page(page_number)
        except PageNotAnInteger:
            page = self.page(1)
        except EmptyPage:
            page = self.page(self.num_pages)
        finally:
            return {
                "notes": list(page) if page else page,
                "has_next": page.has_next(),
                "has_previous": page.has_previous(),
                "current_page": 1 if not page_number else page_number,
            }
