from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    template_name = 'bookmark/list.html'


class BookmarkDetailView(DetailView):
    model = Bookmark
    # template_name을 지정해주지 않으면 bookmark_detail.html으로 자동 지정됨
    template_name = 'bookmark/detail.html'

