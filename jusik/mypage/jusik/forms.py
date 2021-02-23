from django import forms
from jusik.models import Jusik_list

class JusikForm(forms.ModelForm):
    class Meta:
        model = Jusik_list
        fields = ['stock_name','amount','buy_price','sell_price']