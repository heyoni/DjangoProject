# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import CalendarModel
 
class CalendarModelAdmin(admin.ModelAdmin):
    list_display = ['start_day','title']

admin.site.register(CalendarModel, CalendarModelAdmin)


