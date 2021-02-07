from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone

# Create your views here.
def index(request):
    # pybo 목록 출력
    question_list = Question.objects.order_by('-create_date')
    content = {'question_list':question_list}

    # return render(request, 'pybo/question_list.html') # 원래 링크인데, question_list에서 index리스트로 바꿔줬음
    return render(request, 'pybo/index.html', content)


def detail(request, question_id):
    # pybo 내용 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    # pybo 답변 등록
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())

    return redirect('pybo:detail', question_id=question.id)
