from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
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


# 클라우드 처리 기능은 html에서 하므로 코드가 매우 간단함
# {% get_tagcloud %}를 이용하여 설정해준다.
class TagCloudTemplateView(TemplateView):
    template_name = 'taggit/taggit_cloud.html'


# 태그 종류에 따른 리스트를 보여주는 뷰
class TaggedObjectListView(ListView):
    template_name = 'taggit/taggit_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    
    # 기존 메서드 오버라이딩 -> 컨텍스트 변수를 넘겨주기 위함
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # tagname이라는 변수를 새로 추가하고 URL에서 tag 파라미터로 넘어온 값을 넣어줌. -> urls.py에서 'tag/<str:tag>'로 정의해줬었음
        context['tagname'] = self.kwargs['tag']
        return context