from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # pybo 목록 출력

    # 입력 인자
    page = request.GET.get('page','1')
    # 아무것도 입력되어 있지 않으면 첫페이지로 가라는 뜻

    # 조회
    question_list = Question.objects.order_by('-create_date')
    # 역순으로 정렬해서 보여주겠다.

    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # 페이지당 10개만 보여줄것

    content = {'question_list':page_obj}

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
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request):
    # pybo 질문 등록
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # 아직 create_date를 받아오지 않았기 때문에 임시저장 해줌
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

