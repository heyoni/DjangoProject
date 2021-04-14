from django.forms import ModelForm
from django import forms
from articleapp.models import Article
from projectapp.models import Project

class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable', 'style':'height:auto;'}))

    # 프로젝트를 선택하지 않아도 생성가능하게 함
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['title','image','project','content']