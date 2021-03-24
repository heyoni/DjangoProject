from django.urls import path
from . import views


app_name = 'jusik'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:jusik_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('modify/<int:jusik_id>/', views.modify,name='modify'),
    path('delete/<int:jusik_id>/', views.delete,name='delete'),
    path('find/',views.find, name='find'),
    path('find/search/',views.search, name='search'),
]