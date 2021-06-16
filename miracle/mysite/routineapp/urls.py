from django.views.generic import TemplateView
from django.urls import path
from routineapp.views import RoutineListView, RoutineCreateView

app_name = "routineapp"

urlpatterns = [
    path('', RoutineListView.as_view(), name='list'),
    path('create/', RoutineCreateView.as_view(), name='create'),
    # path('detail/<int:pk>', RoutineDetailView.as_view(), name='detail'),
]