from django.db import models

# Create your models here.
class Developer_type(models.Model):
    dev_type = models.CharField(max_length=50)
    count = models.IntegerField(default=0)


class Question(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)


class Choice(models.Model):
    content = models.CharField(max_length=100)
    question = models.ForeignKey(to='main.Question', on_delete=models.CASCADE)
    developer = models.ForeignKey(to='main.developer', on_delete=models.CASCADE, null=True)