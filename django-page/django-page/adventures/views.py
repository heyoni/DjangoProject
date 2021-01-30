from django.shortcuts import render, redirect

# Create your views here.
def input_name(request):
    return render(request, 'input_name.html')


def out(request):
    return render(request, 'out.html')


def get_name(request):
    if request.method == "POST":
        name = request.POST.get('name')

    return render(request,'get_name.html',{'name':name})