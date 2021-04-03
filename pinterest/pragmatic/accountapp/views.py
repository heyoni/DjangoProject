from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from accountapp.models import HelloWorld


# Create your views here.
def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld() # models의 새로운 객체가 new~ 에 저장된다.
        new_hello_world.text = temp # input에서 받은 값을 넣어주기
        new_hello_world.save() # DB에 저장하기

        # hello_world_list = HelloWorld.objects.all() # object list를 모두 보내줌
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list' : hello_world_list}) #이런식으로 사용 시 새로고침하면 기존에 입력했던 값이 계속들어감
        return HttpResponseRedirect(reverse('accountapp:hello_world')) 

    else:
        hello_world_list = HelloWorld.objects.all() # object list를 모두 보내줌
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})
