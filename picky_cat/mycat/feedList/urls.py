from django.urls import path
from feddList.views import FeedListView,FeedListCreateView,FeedListUpdateView,FeedListDeleteView,FeedListDetailView

app_name = 'feedlist'

urlpatterns = [
    path('', FeedListView.as_view(), name='list'),
    path('create/', FeedListCreateView.as_view(), name='create'),
    path('update/<int:pk>', FeedListUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', FeedListDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', FeedListDetailView.as_view(), name='detail'),
]