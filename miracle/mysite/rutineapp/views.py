from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from rutineapp.models import Rutine
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy

from rutineapp.forms import RutineCreationForm

# Create your views here.
class RutineListView(ListView):
    model = Rutine
    context_object_name = 'rutine_list'
    template_name = 'list.html'
    paginate_by = 25
    queryset = Rutine.objects.all()

# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
class RutineCreateiew(CreateView):
    model = Rutine
    form_class = RutineCreationForm
    template_name = 'create.html'
    
    # def form_valid(self, form):
    #     temp_article = form.save(commit=False)
    #     temp_article.writer = self.request.user
    #     temp_article.save()

    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('rutineapp:detail',kwargs={'pk':self.object.pk})