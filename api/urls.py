from django.urls import path

from api.views import PostsList, PostsDetail, PostsCreate

urlpatterns = [
    path('posts/', PostsList.as_view(), name='posts_list'),
    path('posts/new/', PostsCreate.as_view, name='post_new'),
    path('posts/<int:pk>/', PostsDetail.as_view(), name='post_detail'),
]