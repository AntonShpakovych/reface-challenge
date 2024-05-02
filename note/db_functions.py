from django.db import models
from django.db.models import Func


class CountUniqueWords(Func):
    function = "count_unique_words"
    template = "%(function)s(%(expressions)s)"
    output_field = models.IntegerField()


class CountWords(Func):
    function = "count_words"
    template = "%(function)s(%(expressions)s)"
    output_field = models.IntegerField()
