from django import forms

class PostSearchForm(forms.Form):
    # 입력폼을 만들었음, 즉 html 요소 <input type='text'>를 만든것
    search_word = forms.CharField(label='Search Word')

