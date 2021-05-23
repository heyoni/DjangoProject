from django.urls import path
from . import views

app_name = 'calendarapp'

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('input/', views.event, name='input'),
    path('edit/<int:event_id>', views.event, name="edit"),
]

