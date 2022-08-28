from django.core.exceptions import ValidationError


def start_with_09(value):
    if value[0:2] != '09':
        raise ValidationError('شماره تلفن باید با 09 شروع شود')


def is_digit(value):
    if not value.isdigit():
        raise ValidationError('شماره موبایل باید به صورت عددی باشد')
