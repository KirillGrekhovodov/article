from django import template

register = template.Library()


@register.filter
def shorten(value, arg):
    result = value[:arg]
    if value != result:
        result += "..."
    return result
