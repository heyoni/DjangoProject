from django.db import models

# Create your models here.
class Jusik_list(models.Model):
    stock_name = models.CharField(max_length=200)
    date = models.DateField(default='2020-02-23')
    amount = models.IntegerField()
    buy_price = models.IntegerField()
    amount_buy = models.IntegerField(default=0)
    sell_price = models.IntegerField()
    amount_sell = models.IntegerField(default=0)
    result = models.IntegerField(default=0)
    present_price = models.IntegerField(default=0)                                                                   )

    def __str__(self):
        return self.stock_name