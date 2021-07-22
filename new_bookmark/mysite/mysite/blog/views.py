from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView


from blog.models import Post
from django.conf import settings

from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['discuss_title'] = f"{self.object.slug}"
        return context

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


# FormView 제네릭뷰는 Get요청인 경우에는 폼을 화면에 보여주고 사용자의 입력을 기다림
# 사용자가 폼을 입력 후 제출하면 Post 요청으로 접수되며 FormView에서 유효성 검사를 하고 
# 데이터가 유효하면 form_valid() 함수를 실행하고 적절한 url로 보내줌.
class SearchFormView(FormView): 
    form_class = PostSearchForm 
    template_name = 'blog/post_search.html' 

    def form_valid(self, form): 
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) |  Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {} 
        context['form'] = form 
        context['search_term'] = searchWord 
        context['object_list'] = post_list 

        return render(self.request, self.template_name, context)   # No Redirection