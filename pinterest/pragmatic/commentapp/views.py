from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})