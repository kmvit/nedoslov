from django.contrib import admin
from actors.models import Actors

# Register your models here.
class ActorsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Actors,ActorsAdmin)
