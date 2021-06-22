from django.shortcuts import render
from routineapp.models import Routine
from django.views.generic import ListView


# Create your views here.
class InfoListView(ListView):
    model = Routine
    context_object_name = 'routine_info'
    template_name = 'infoapp/info.html'
    paginate_by = 25
    queryset = Routine.objects.all()