from django.views.generic import TemplateView
from django.urls import path
from routineapp.views import RoutineListView, RoutineCreateView,RoutineUpdateView

app_name = "routineapp"

urlpatterns = [
    path('', RoutineListView.as_view(), name='list'),
    path('create/', RoutineCreateView.as_view(), name='create'),
    path('update/<int:pk>', RoutineUpdateView.as_view(), name='update'),
]