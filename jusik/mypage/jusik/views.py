from django.shortcuts import render
from .models import Jusik_list


def index(request):
    # 주식 목록 출력
    jusik_list = Jusik_list.objects.order_by('buy_date')
    context = {'jusik_list':jusik_list}
    return render(request, 'jusik/index.html', context)


def detail(request, jusik_id):
    # 주식 내용 출력(구체적)
    jusik = Jusik_list.objects.get(id=jusik_id)
    context = {'jusik':jusik}
    return render(request, 'jusik/jusik_detail.html',context)