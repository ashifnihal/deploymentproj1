from django import template
register=template.Library()
@register.filter(name='f2lower')
def first_two_chars(value):
    result=value[0:10].lower()
    return result
# register.filter('f2lower',first_two_chars)
