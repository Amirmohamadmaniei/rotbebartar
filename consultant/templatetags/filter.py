import datetime
from django import template

register = template.Library()


@register.filter(name='int_for_loop')
def int_for_loop(value):
    return range(int(value))


@register.filter(name='ration_to_text')
def ration_to_text(value):
    if value == '1':
        return 'منطقه یک'
    elif value == '2':
        return 'منطقه دو'
    elif value == '3':
        return 'منطقه سه'
    elif value == '4':
        return 'ایثارگران 5 درصد'
    elif value == '5':
        return 'ایثارگران 25 درصذ'
    elif value == '6':
        return 'هیئت علمی'


@register.filter(name='grade_to_text')
def grade_to_text(value):
    if value == '10':
        return 'دهم'
    elif value == '11':
        return 'یازدهم'
    elif value == '12':
        return 'دوازدهم'
    elif value == 'posht_konkoor':
        return 'پشت کنکوری'


@register.filter(name='major_high_school_to_text')
def major_high_school_to_text(value):
    if value == 'riazi':
        return 'ریاضی'
    elif value == 'tajrobi':
        return 'تجربی'
    elif value == 'ensani':
        return 'انسانی'
    elif value == 'fani':
        return 'فنی و حرفه ای'
    elif value == 'tarbiat_badani':
        return 'تربیت بدنی'


@register.filter(name='price')
def price(value, month):
    if month == 1:
        return value
    elif month == 2:
        return str((int(value) - int(value) * 5 // 100) * month)
    elif month == 3:
        return str((int(value) - int(value) * 10 // 100) * month)
    elif month == 6:
        return str((int(value) - int(value) * 15 // 100) * month)
    elif month == 12:
        return str((int(value) - int(value) * 25 // 100) * month)


@register.filter(name='separator')
def separator(value):
    value = str(value[::-1])
    count = 0
    value2 = ''
    for i in value:
        if count % 3 == 0 and count != 0:
            value2 += ','
        count += 1
        value2 += i
    return value2[::-1]
