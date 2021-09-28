# I have created this file - Surya

from django.shortcuts import render, get_object_or_404 
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# from django.http import HttpResponse

# importing class based views
from django.views.generic import  (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)


# Create your views here.
# home func handles the traffic from the home page of blog
# blog_project -> blog -> templates -> blog -> templates.html

# function based view ->
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# class based views ->

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5



# view for all posts by a user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post

    # naming convention for template name
    # <app>/<model>_<viewtype>.html



class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    fields = [ 'title', 'content' ]
    
    # override the form_valid() method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [ 'title', 'content' ]
    
    # override the form_valid() method
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



# about func handles the traffic from the about page of blog
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



# funtions based views-
# urlpatterns are directed to a certain view which are these funtions
# and the views then handle the logic for the route and then render our template

# class based views->
# class based views provide a lot more built in functionality that handles a lot of back end logic by itself
# examples are ListView, CreateView, UpdateView, DeleteView, etc..
