from django import template
register = template.Library()


@register.filter
def sum_miracle_time(value):
    sum = 0
    result = str(value).split('>')
    for i in result[:-2]:
        i = i.split(',')[-1]
        sum += int(i)
    
    
    return sum
