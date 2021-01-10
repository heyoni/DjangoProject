from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/를 호출했을 때 view에 있는 index 메서드를 호출한다.
    path('', views.index, name='index'),

    # /polls/숫자/ 를 호출했을 때 상세페이지를 보여준다.
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]