from django.urls import path
from . import views

app_name = 'calendarapp'

urlpatterns = [
    path('', views.CalendarView, name='calendar'),
]