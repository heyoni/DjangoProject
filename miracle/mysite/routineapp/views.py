from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from routineapp.models import Routine
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

from routineapp.forms import RoutineCreationForm

# Create your views here.
class RoutineListView(ListView):
    model = Routine
    context_object_name = 'routine_list'
    template_name = 'routineapp/list.html'
    paginate_by = 25
    queryset = Routine.objects.all()

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class RoutineCreateView(CreateView):
    model = Routine
    form_class = RoutineCreationForm
    template_name = 'routineapp/create.html'
    
    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('routineapp:list')


# class RoutineDetailView(DetailView, FormMixin):
#     model = Routine
#     form_class = CommentCreationForm

#     context_object_name = 'target_routine'
#     template_name = 'routineapp/detail.html'