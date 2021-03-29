from django.shortcuts import render, get_object_or_404, redirect
from .models import Jusik_list
from .forms import JusikForm
from .parser import get_price, get_code
from .graph import get_graph

from django.conf import settings
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def index(request):
    # 주식 목록 출력
    jusik_list = Jusik_list.objects.order_by('-date')
    context = {'jusik_list':jusik_list}
    return render(request, 'jusik/index.html', context)


def detail(request, jusik_id):
    # 주식 내용 출력(구체적)
    jusik = get_object_or_404(Jusik_list, pk=jusik_id)
    get_graph(jusik.stock_code)
    context = {'jusik':jusik}
    return render(request, 'jusik/jusik_detail.html',context)


def create(request):
    # 주식 등록
    if request.method == 'POST':
        form = JusikForm(request.POST)
        name = request.POST.get('stock_name')
        code = request.POST.get('stock_code')

        if form.is_valid():
            jusik = form.save(commit=False)
            jusik.present_price = get_price(code)
            jusik.stock_name = name
            jusik.stock_code = code

            jusik.save()

            return redirect('jusik:index')

    else:
        form = JusikForm()
        name = ''
        code = ''
    context = {'form':form, 'name':name, 'code':code}
    return render(request, 'jusik/create.html', context)


def modify(request, jusik_id):
    # 입력정보 수정
    jusik = get_object_or_404(Jusik_list, pk=jusik_id)

    if request.method == 'POST':
        form = JusikForm(request.POST, instance=jusik)
        if form.is_valid():
            jusik = form.save(commit=False)
            jusik.save()
            return redirect('jusik:detail', jusik_id=jusik.id)
    else:
        form = JusikForm(instance=jusik)
    context = {'form':form}
    return render(request, 'jusik/create.html',context)


def delete(request, jusik_id):
    # 삭제
    jusik = get_object_or_404(Jusik_list, pk=jusik_id)
    jusik.delete()
    return redirect('jusik:index')


def find(request):
    return render(request, 'jusik/find.html')



def search(request):
    stock_name = request.POST.get('code_input')
    apikey = settings.SECRET_KEY

    url = f'http://api.seibro.or.kr/openapi/service/StockSvc/getStkIsinByNmN1?serviceKey={apikey}&secnNm={stock_name}&numOfRows=50&pageNo=1'

    
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    items = soup.findAll('item')
    arr = []
    for item in items:
        name = item.find('korsecnnm').text
        code = item.find('shotnisin').text
        arr.append([name, code])
        if len(arr) > 50:
            break
    context = {'arr':arr}
    return render(request,'jusik/find.html',context)