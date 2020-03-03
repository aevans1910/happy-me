from django.urls import path
from blog.views import PostsListView, PostsDetailView, PostsCreateView

urlpatterns = [
    path('', PostsListView.as_view(), name='blog-list-page'),
    path('new/', PostsCreateView.as_view(), name='new'),
    path('<str:slug>/', PostsDetailView.as_view(), name='blog-details-page'),
]