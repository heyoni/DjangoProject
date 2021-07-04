# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import CalendarModel
 
class CalendarModelAdmin(admin.ModelAdmin):
<<<<<<< Updated upstream
    list_display = ['start_day','title','time']
=======
    list_display = ['start_time','title']
>>>>>>> Stashed changes

admin.site.register(CalendarModel, CalendarModelAdmin)


