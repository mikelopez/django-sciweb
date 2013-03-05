from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def cut_text(text, amount):
    """
    show the first 'x' characters.
    default first characters to show is 245
    """
    if len(text) > int(amount):
        text = text[:int(amount)] + '...'
        try:
            return str(text)
        except:
            return text[:int(amount)]
   
    return text
    



