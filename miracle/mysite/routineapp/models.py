from django.db import models

# Create your models here.
class Routine(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(max_length=500,null=True)
    time = models.IntegerField(default=0)
    color = models.CharField(max_length=150,default='black',null=True)
    
    def __str__(self):
        return self.title


        