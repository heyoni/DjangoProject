from django.shortcuts import render, get_object_or_404, redirect

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from projectapp.models import Project
from subscribeapp.models import Subscription
from articleapp.models import Article
from django.views.generic import CreateView, DetailView, ListView

from django.views.generic import RedirectView
from django.urls import reverse
 


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # project_pk를 get 방식으로 받아서 pk를 가지고있는 detail 페이지로 이동
        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # 찾는게 없으면 404에러로 넘겨줌
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        
        # project, user의 값을 통해서 subscription을 찾아줌
        subscription = Subscription.objects.filter(user=user, project=project)

        # 구독정보가 있으면 구독취소 없으면 구독
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)


# field Lookup을 이용하여 구독페이지 만들기
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    pagenate_by = 5

    def get_queryset(self):
        # 구독한 모든 프로젝트를 리스트화 함
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # projects를 기반으로 하여 field lookup으로 구현
        article_list = Article.objects.filter(project__in=projects)
        return article_list 