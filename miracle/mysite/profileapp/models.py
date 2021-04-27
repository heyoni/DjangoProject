from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    # OneToOne : profile, user를 하나씩 연결해주는 역할, django에서 제공
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    image = models.ImageField(upload_to='profile/',null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)