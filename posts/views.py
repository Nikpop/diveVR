from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import  ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
import json

from .models import Posts

class PostsListView(ListView):
    model = Posts
    template_name = 'posts_list.html'

class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts_detail.html'

class PostsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ('title', 'body')
    template_name = 'posts_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    template_name = 'posts_delete.html'
    success_url = reverse_lazy('posts_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author ==self.request.user


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'posts_new.html'
    fields = ('title', 'body', 'background')
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def check_user_name(request):
        if request.GET:
            background = request.GET[""]