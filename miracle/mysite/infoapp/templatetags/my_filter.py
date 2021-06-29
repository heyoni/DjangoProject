from django import template

register = template.Library()


@register.filter
def sumFor(value):
    result = 0
    for i in value:
        result += int(i.time)

    return result

def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')