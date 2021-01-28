from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main.html')
    # 메인이라는 함수는 요청이 날아오면 request에 대응을 해서 main.html을 보여주겠다
    # (보통 render의 함수명과 경로 명을 일치시켜줌)


def test(request):
    return render(request, 'test.html')