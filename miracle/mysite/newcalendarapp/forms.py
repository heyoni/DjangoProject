from django.forms import ModelForm, DateInput
from .models import CalendarModel

class CalendarModelForm(ModelForm):
    class Meta:
        model = CalendarModel
        widgets = {
            'start_time': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(CalendarModelForm, self).__init__(*args, **kwargs)
        self.fields['start_time'].input_formats = ('%Y-%m-%d',)