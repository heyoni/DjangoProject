from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project


class Subscription(models.Model):
    # user - project간 구독 정보가 딱 하나가 되도록 만들 것
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscript')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscript')

    # 구독정보는 하나이기 떄문에 아래에서 처리해줌
    class Meta:
        unique_together = ('user','project')