from calendar import Calendar
# from mysite.newcalendarapp.models import CalendarModel
from django.shortcuts import render
from newcalendarapp.models import CalendarModel
from django.views.generic import ListView


# Create your views here.
class InfoListView(ListView):
    model = CalendarModel
    context_object_name = 'CalendarModel_info'
    template_name = 'infoapp/info.html'
    queryset = CalendarModel.objects.all()