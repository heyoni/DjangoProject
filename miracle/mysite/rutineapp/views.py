from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from rutineapp.models import Rutine
from django.core.paginator import Paginator

from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy


# Create your views here.
class RutineListView(ListView):
    model = Rutine
    context_object_name = 'rutine_list'
    template_name = 'list.html'
    paginate_by = 25
    queryset = Rutine.objects.all()


# class RutineCreateiew(CreateView):
#     model = Rutine
#     form_class = 