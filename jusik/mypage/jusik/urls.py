from django.urls import path
from . import views


app_name = 'jusik'

urlpatterns = [
    path('', views.index, name='index'),
]