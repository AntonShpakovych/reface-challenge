from django.db import models
from django.db.models import Func


class CountUniqueWords(Func):
    """
    Count the number of unique words in the given text
    """
    function = "count_unique_words"
    template = "%(function)s(%(expressions)s)"
    output_field = models.IntegerField()


class CountWords(Func):
    """
    Count the number of words in the given text
    """
    function = "count_words"
    template = "%(function)s(%(expressions)s)"
    output_field = models.IntegerField()
