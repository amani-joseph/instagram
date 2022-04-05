from importlib import import_module
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from users_app.models import Profile


# Create your views here.
# PostViews
class PostListView(ListView):
    model = Post
    template_name = 'insta/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-pub_date']
    
    
class AuthorDetailView(DetailView):
    model = Profile
    template_name = 'users_app/not_user_profile.html' 
# PostViews
def index(request):
    local_posts = [{
        "image": "https://images.pexels.com/photos/5989067/pexels-photo-5989067.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "likes": "600",
        "comments": ["Dope", "Capping", "Big up my dawg!!"],
        "pub_date": "Mar 2, 2022",
        "caption": "Life on the fast lane",
        "user": "John Doe"
        # comment: ""
    },
        {
            "image": "https://images.pexels.com/photos/9125253/pexels-photo-9125253.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "likes": "600",
            "comments": ["Dope", "Capping", "Big up my dawg!!"],
            "pub_date": "Mar 2, 2022",
            "caption": "Life on the fast lane",
            "user": "John Doe"
            # comment: ""
        },
        {
            "image": "https://images.pexels.com/photos/7614448/pexels-photo-7614448.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "likes": "600",
            "comments": ["Dope", "Capping", "Big up my dawg!!"],
            "pub_date": "Mar 2, 2022",
            "caption": "Life on the fast lane",
            "user": "John Doe"
            # comment: ""
        },
        {
            "image": "https://images.pexels.com/photos/7478690/pexels-photo-7478690.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
            "likes": "600",
            "comments": ["Dope", "Capping", "Big up my dawg!!"],
            "pub_date": "Mar 2, 2022",
            "caption": "Life on the fast lane",
            "user": "John Doe"
            # comment: ""
        },
    ]
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'insta/index.html', context)
