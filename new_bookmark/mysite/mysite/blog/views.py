from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView


from blog.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class PostArchiveView(ArchiveIndexView):
    model = Post
    # 변경날짜가 최근인 포스트 먼저 표기
    date_field = 'modify_dt'
    template_name = 'blog/archive.html'



class PostYearArchiveView(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    template_name = 'blog/archive_year.html'


class PostMonthArchiveView(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'blog/archive_month.html'



class PostDayArchiveView(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'blog/archive_day.html'


class PostTodayArchiveView(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    template_name = 'blog/archive_today.html'


