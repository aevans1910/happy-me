from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from blog.models import Posts
from blog.forms import PostsForm

class PostsListView(ListView):
    """ Renders a list of all the Posts """
    model = Posts

    def get(self, request):
        """ GET a list of Posts """
        posts = self.get_queryset().all()
        return render(request, 'blog/list.html', {
            'posts': posts
        })

class PostsDetailView(DetailView):
    """ Renders a specific post based on it's slug """
    model = Posts

    def get(self, request, slug):
        """ Returns a specific blog post by slug """
        post = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'blog/post.html', {
            'post': post
        })

class PostsCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': PostsForm()}
        return render(request, 'blog/new.html', context)

    def post(self, request, *args, **kwargs):
        form = PostsForm(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect(reverse_lazy('blog-list-page'))
        return render(request, 'blog/new.html', {'form':form})