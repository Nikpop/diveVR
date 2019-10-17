from django.urls import path

from .views import PostsListView, PostsUpdateView, PostsDetailView, PostsDeleteView, PostsCreateView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
    path('<int:pk>/edit/', PostsUpdateView.as_view(), name='posts_edit'),
    path('<int:pk>/', PostsDetailView.as_view(), name='posts_detail'),
    path('<int:pk>/delete/', PostsDeleteView.as_view(), name='posts_delete'),
    path('new/', PostsCreateView.as_view(), name='posts_new'),
]