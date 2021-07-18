from django.urls import path
from bookmark.views import BookmarkListView,BookmarkDetailView

app_name = 'bookmarkapp'
urlpatterns = [
    path('',BookmarkListView.as_view(),name='list'),
    path('<int:pk>/',BookmarkDetailView.as_view(), name='detail')
]