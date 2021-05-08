from django.views.generic import TemplateView
from django.urls import path
from rutineapp.views import RutineListView, RutineCreateView

app_name = "rutineapp"

urlpatterns = [
    path('', RutineListView.as_view(), name='list'),
    path('create/', RutineCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', RutineDetailView.as_view(), name='detail'),
]