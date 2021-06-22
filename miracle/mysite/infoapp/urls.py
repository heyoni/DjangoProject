from django.urls import path
from infoapp.views import InfoListView
app_name = 'infoapp'

urlpatterns = [
    # path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
    path('', InfoListView.as_view() ,name='info')
]