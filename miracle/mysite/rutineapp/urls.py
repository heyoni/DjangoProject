from django.views.generic import TemplateView
from django.urls import path
from rutineapp.views import RutineListView

app_name = "rutineapp"

urlpatterns = [
    path('', RutineListView.as_view(), name='list'),

]