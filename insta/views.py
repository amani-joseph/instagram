from dataclasses import fields
from importlib import import_module
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from .forms import UploadForm
from users_app.models import Profile
from django.contrib.auth.models import User


# Create your views here.
# PostViews
class PostListView(ListView):
    model = Post
    template_name = 'insta/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-pub_date']
    paginate_by = 5
    
    
class AuthorDetailView(DetailView):
    model = Profile
    template_name = 'users_app/not_user_profile.html'
    
    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs)  
        
        model = Post.objects.all()                 
    #     posts = [{
    #     "image": "https://images.pexels.com/photos/5989067/pexels-photo-5989067.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
    #     "likes": "600",
    #     "comments": ["Dope", "Capping", "Big up my dawg!!"],
    #     "pub_date": "Mar 2, 2022",
    #     "caption": "Life on the fast lane",
    #     "user": "John Doe"
    #     # comment: ""
    # },
    #     {
    #         "image": "https://images.pexels.com/photos/7478690/pexels-photo-7478690.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
    #         "likes": "600",
    #         "comments": ["Dope", "Capping", "Big up my dawg!!"],
    #         "pub_date": "Mar 2, 2022",
    #         "caption": "Life on the fast lane",
    #         "user": "John Doe"
    #         # comment: ""
    #     },
    # ]
        context["posts"] = model
        return context
    
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['image', 'caption', 'hashtags']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(PostCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('insta-home')
    
    
    
# PostViews
# def PostCreate(request):
#     form = UploadForm
#     context= {
#         "form": form
#     }
#     if request.method == 'POST':
#         currentUser = request.user
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post()
#             post.caption = form.cleaned_data.get('caption')
#             print(post.caption)
#             post.image = form.cleaned_data.get('image')
#             post.hashtags = form.cleaned_data.get('hashtags')
#             post.save()
#             return redirect('insta-home')
#     return render(request, 'insta/post_form.html', context)

# if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created {username} \n welcome to instagram')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, "users_app/register.html", {'form': form})

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
