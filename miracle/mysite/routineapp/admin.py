from django.contrib import admin
from .models import Routine

class RoutineAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Routine, RoutineAdmin)