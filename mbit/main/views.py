from django.shortcuts import render
from .models import Question, Developer, Choice

def index(request):
    developers = Developer.objects.all()
    # print(developers)
    # print(type(developers))
    # print(dir(developers))
    context = {'developers': developers,}
    return render(request, 'index.html', context=context)


def form(request):
    questions = Question.objects.all()
    context = {'questions': questions,}
    return render(request, 'form.html', context)


def result(request):
    return render(request, 'result.html')