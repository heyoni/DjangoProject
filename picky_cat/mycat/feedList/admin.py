# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import FeedList
 
class FeedListModelAdmin(admin.ModelAdmin):
    list_display = ['name','crude_protein','crude_Fat','phosphorus','palatability']

admin.site.register(FeedList, FeedListModelAdmin)


