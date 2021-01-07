from django.db import models

# Create your models here.
# 게시물과 관련된 클래스, 모델은 기본적으로 클래스로 구성됨
# 클래스는 모델을 상속함
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()  
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)

# 이 모델을 생성했고 데이터베이스에 생성시켜줘야함
# -> 터미널 ./manage.py makemigrations community로 변화를 확인해주고
# -> ./manage.py migrate를 하면 db.sqlite3에 생성됨
