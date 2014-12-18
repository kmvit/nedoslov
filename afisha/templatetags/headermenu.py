from django import template
from afisha.models import Headermenu


register = template.Library()
@register.inclusion_tag("headermenu.html")
def show_headmenu():
    menu = Headermenu.objects.all()
    context_dict ={'menu': menu}
    return context_dict
