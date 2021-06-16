from django.forms import ModelForm
from django import forms
from rutineapp.models import Rutine

class RutineCreationForm(ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable', 'style':'height:auto;'}))

    class Meta:
        model = Rutine
        fields = '__all__'