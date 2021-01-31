from django.urls import path
from . import views

urlpatterns = [
    path('input_name/', views.input_name, name='input_name'),
    path('out/', views.out, name='out'),
    path('get_name/', views.get_name, name='get_name'),
    path('check_number/', views.check_number, name='check_number'),
    path('success/', views.success, name='success'),

]