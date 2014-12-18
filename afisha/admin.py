from django.contrib import admin
from afisha.models import Carousel,Headermenu

class HeadermenuAdmin(admin.ModelAdmin):
    list_display = ('name','url')

# Register your models here.
admin.site.register(Carousel)
admin.site.register(Headermenu, HeadermenuAdmin)
