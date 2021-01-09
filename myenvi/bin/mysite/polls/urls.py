from django.urls import path

# views 호출하려면 -> 연결된 URL 필요, 이를 위해서 URLconf가 사용됨
# URLconf를 생성하려면 이 파일을 생성해야한다.

# views를 호출하기 위해서 작성하는 코드
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# 그 다음에는 최상위 URLconf에서 polls.urls 모듈을 연결해줘야함
# 그러면 mysite/urls에서 import해줌