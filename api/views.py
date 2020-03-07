from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Posts
from blog.forms import PostsForm
from api.serializers import PostsSerializer

class PostsList(APIView):
    def get(self, request):
        posts = Posts.objects.all()[:5]
        data = PostsSerializer(posts, many=True).data
        return Response(data)

class PostsDetail(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        data = PostsSerializer(post).data
        return Response(data)

    def delete(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        post.delete()

    def put(self, request, pk):
        post = get_object_or_404(Posts, pk=pk)
        form = PostsForm(request.POST)
        data = PostsSerializer(form).data
        return Response(data)

class PostsCreate(APIView):
    def post(self, request):
        form = PostsForm(request.POST)
        data = PostsSerializer(form).data
        return Response(data)
