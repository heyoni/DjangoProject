from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='사료 이름', max_length=50)
    crude_protein = models.IntegerField(blank=True)
    crude_Fat = models.IntegerField(blank=True)
    phosphorus = models.IntegerField(blank=True)

    CHOICE = {
        ('LIKE','DISLIKE')
    }
    palatability = models.CharField(max_length=2, choices=CHOICE)

    def __str__(self):
        return self.name