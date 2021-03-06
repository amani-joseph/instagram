import imp
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from insta.models import Post
from django.http import HttpResponse


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username} \n welcome to instagram')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "users_app/register.html", {'form': form})


@login_required
def profile(request):
    context = {
        'posts': Post.objects.filter(user=request.user).all()
    }
    return render(request, 'users_app/profile.html',context )


@login_required
def author_profile(request):
    context = {
        'posts': Post.objects.filter(user=request.user).all(),
        
    }
    # if request.user == Post.objects.post.user:  
    return redirect('profile')
    # else:
    #     return render(request, 'users_app/not_user_profile.html',context )


@login_required
def editProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users_app/edit_profile.html', context)
