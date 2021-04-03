from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from accountapp.forms import AccountUpdateForm
from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld


has_ownership = [account_ownership_required, login_required]

# Create your views here.

@login_required
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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login') 
    template_name = 'accountapp/delete.html'
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()