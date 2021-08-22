from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

# Create your views here.
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from feedList.models import ArtiFeedListcle

from django.core.paginator import Paginator



class FeedListCreateView(CreateView):
    model = FeedList
    template_name = 'feedlist/create.html'

    def form_valid(self, form):
        temp_feed = form.save(commit=False)
        temp_feed.writer = self.request.user
        temp_feed.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('feedlist:detail',kwargs={'pk':self.object.pk})


class FeedListDetailView(DetailView, FormMixin):
    model = FeedList

    context_object_name = 'target_feed'
    template_name = 'feedlist/detail.html'


class FeedListUpdateView(UpdateView):
    model = FeedList
    context_object_name = 'target_feed'
    template_name = 'feedlist/update.html'


    def get_success_url(self):
        return reverse('feedlist:detail',kwargs={'pk':self.object.pk})


# @method_decorator(article_ownership_required, 'get')
# @method_decorator(article_ownership_required, 'post')
class FeedListDeleteView(DeleteView):
    model = FeedList
    context_object_name = 'target_feed'
    template_name = 'feedlist/delete.html'
    success_url = reverse_lazy('feedlist:list')


class FeedListListView(ListView):
    model = FeedList
    context_object_name = 'target_feed'
    template_name = 'feedlist/list.html'
    paginate_by = 25
    queryset = FeedList.objects.all()