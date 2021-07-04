from django.urls import path
from . import views
from newcalendarapp.views import calendarDeleteView

app_name = 'calendarapp'

urlpatterns = [
    path('', views.calendarView, name='calendar'),
    path('input/', views.event, name='input'),
    path('edit/<int:event_id>', views.event, name="edit"),
    path('delete/<int:pk>', calendarDeleteView.as_view(), name="delete"),
]
