from django.core.exceptions import ValidationError


def min_select(min_items):
    def validator(values):
        if len(values) < min_items:
            raise ValidationError(
                "At least {} values must be selected".format(min_items))
    return validator


def max_select(max_items):
    def validator(values):
        if len(values) > max_items:
            raise ValidationError(
                "At most {} values can be selected".format(max_items))
    return validator

