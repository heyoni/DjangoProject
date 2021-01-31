from django.shortcuts import render, redirect

import pdb
from random import *

# Create your views here.
def input_name(request):
    return render(request, 'input_name.html')


def out(request):
    return render(request, 'out.html')


def get_name(request):
    if request.method == "POST":
        name = request.POST.get('name')
    return render(request,'get_name.html',{'name':name})


def check_number(request):
    if request.method == "POST":
        user_number = int(request.POST.get('user_number'))
        random_number = randint(1, 3)
        # pdb.set_trace()
        if user_number == random_number:
            return redirect('success')
        else:
            return redirect('out')



def success(request):
    return render(request, 'success.html')


