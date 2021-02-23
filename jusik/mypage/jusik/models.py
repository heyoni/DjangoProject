from django.db import models

# Create your models here.
class Jusik_list(models.Model):
    buy_date = models.DateTimeField()
    stock_name = models.CharField(max_length=200)
    amount = models.IntegerField()
    buy_price = models.IntegerField()
    buy_amount = models.IntegerField()
    sell_price = models.IntegerField()
    sell_amount = models.IntegerField()
    profit = models.IntegerField()

    def __str__(self):
        return self.stock_name