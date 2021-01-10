import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 어떤 데이터가 들어왔는지 더 명확하게 알기 위해서 작성
    def __str__(self):
        return self.question_text
    
    # 커스텀 메소드 : 어제 발행된 데이터들을 찾아줌 
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    # 어떤 데이터가 들어왔는지 더 명확하게 알기 위해서 작성
    def __str__(self):
        return self.choice_text