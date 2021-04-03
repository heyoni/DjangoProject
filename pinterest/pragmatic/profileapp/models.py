from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    # OnetoOne : profile, user를 하나씩 연결해주는 역할, django에서 제공
    user = models.OnetoOneFiled(User, on_delete=models.CASCADE)