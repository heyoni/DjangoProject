from django import forms
from pybo.models import Question, Answer, Comment

# 장고폼, 장고에서 기본적으로 제공함
# 폼과 모델폼이 있는데 여기서는 모델을 상속받았으므로 모델폼이라고 함
# 모델과 연결된 폼이며 모델폼 객체를 저장하면 연결된 모델의 데이터를 저장할 수 있따


class QuestionForm(forms.ModelForm):
    class Meta: # 이 클래스가 반드시 필요
        model = Question # 모델 : Question과 연결되어있음을 뜻함
        fields = ['subject', 'content']# 모델의 필드
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content':'댓글 내용',
        }