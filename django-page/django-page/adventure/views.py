from django.shortcuts import render

def first(request):
    return render(request, 'first.html')


def second(request):
    return render(request, 'second.html')


def third(request):
    return render(request, 'third.html')


def fourth(request):
    if request.method == "POST":
       your_name = request.POST.get('name')
    return render(request, 'fourth.html', {'name1' : your_name})
