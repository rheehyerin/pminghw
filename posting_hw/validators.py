import requests
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible
from django.conf import settings


@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError("Error")