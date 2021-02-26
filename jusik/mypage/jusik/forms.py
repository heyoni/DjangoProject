from django import forms
from jusik.models import Jusik_list

class JusikForm(forms.ModelForm):
    class Meta:
        model = Jusik_list
        fields = ['stock_name','amount','buy_price','sell_price']
        labels = {
            'stock_name' : '종목명',
            'amount' : '수량',
            # 'buy_price' : '매수가격',
            'sell_price' : '매도가격',
            'date' : '날짜'
        }