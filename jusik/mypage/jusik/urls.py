from django.urls import path
from . import views


app_name = 'jusik'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:jusik_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]