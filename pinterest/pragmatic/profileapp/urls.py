from django.urls import path
from profileapp.views import ProfileCreationForm

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreationForm.as_view(), name='create'),
]