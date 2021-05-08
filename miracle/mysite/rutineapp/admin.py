from django.contrib import admin
from .models import Rutine


class RutineAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Rutine, RutineAdmin)