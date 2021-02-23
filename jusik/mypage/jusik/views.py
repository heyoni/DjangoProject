from django.shortcuts import render, get_object_or_404
from .models import Jusik_list


def index(request):
    # 주식 목록 출력
    jusik_list = Jusik_list.objects.order_by('buy_date')
    context = {'jusik_list':jusik_list}
    return render(request, 'jusik/index.html', context)


def detail(request, jusik_id):
    # 주식 내용 출력(구체적)
    jusik = get_object_or_404(Jusik_list, pk=jusik_id)
    context = {'jusik':jusik}
    return render(request, 'jusik/jusik_detail.html',context)


def jusik_create(request):
    # 주식 등록
    form = JusikForm()
    return render(request, 'jusik/jusik_form.html', {'form':form})