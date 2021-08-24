# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Profile
 
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','image','nickname','message']

admin.site.register(Profile, ProfileModelAdmin)


