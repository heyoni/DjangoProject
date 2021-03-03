from django import forms
from jusik.models import Jusik_list

class JusikForm(forms.ModelForm):
    class Meta:
        model = Jusik_list
        fields = ['date','stock_name','amount','buy_price','amount_buy','sell_price','amount_sell','result']
        labels = {
            'date' : '날짜',
            'stock_name' : '종목명',
            'amount' : '수량',
            'buy_price' : '매수가격',
            'amount_buy' : '총 매수가격',
            'sell_price' : '매도가격',
            'amount_sell' : '총 매도가격',
            'result' : '총 수익',
            'present_price' : '현재 가격',
        }