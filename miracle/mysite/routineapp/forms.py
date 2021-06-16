from django.forms import ModelForm
from django import forms
from routineapp.models import Routine

class RoutineCreationForm(ModelForm):
    # content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable', 'style':'height:auto;'}))

    class Meta:
        model = Routine
        fields = '__all__'