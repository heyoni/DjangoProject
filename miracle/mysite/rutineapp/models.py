from django.db import models

# Create your models here.
class Rutine(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=150,default='red',null=True)


    def __str__(self):
        return f'{self.title},{self.color}'