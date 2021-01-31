from django.urls import path
from . import views


urlpatterns = [
    path('first/', views.first, name="first"),
    path('second/', views.second, name="second"),
    path('third/', views.third, name="third"),
    path('fourth/', views.fourth, name="fourth"),

]