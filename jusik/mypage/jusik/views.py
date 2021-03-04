from django.shortcuts import render, get_object_or_404, redirect
from .models import Jusik_list
from .forms import JusikForm
from .parser import get_price


def index(request):
    # 주식 목록 출력
    jusik_list = Jusik_list.objects.order_by('stock_name')
    context = {'jusik_list':jusik_list}
    return render(request, 'jusik/index.html', context)


def detail(request, jusik_id):
    # 주식 내용 출력(구체적)
    jusik = get_object_or_404(Jusik_list, pk=jusik_id)
    context = {'jusik':jusik}
    return render(request, 'jusik/jusik_detail.html',context)


def create(request):
    # 주식 등록
    if request.method == 'POST':
        form = JusikForm(request.POST)
        if form.is_valid():
            jusik = form.save(commit=False)
            # 주식 종목명 가져오기(구현 필요) 
            
            # 주식 현재가 가져오기
            jusik.present_price = get_price('005930')
            jusik.save()
            return redirect('jusik:index')

    else:
        form = JusikForm()
    context = {'form':form}
    return render(request, 'jusik/create.html', context)