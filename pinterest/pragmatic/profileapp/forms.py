from django.forms import ModelForm
from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = ProfileCreationForm
        fields = ['image', 'nickname', 'message']