from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.product_list, name='list'),
    path('<int:id>/', views.product_detail, name='detail'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]