from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post





class UploadForm(forms.ModelForm):
    '''
    Class that handles forms
    '''
    class Meta:
        model = Post
        fields = ['image', 'caption', 'hashtags']
        exclude = ["likes", "pub_date", "comments", "user"]
        
        
# class CommentForm(forms.ModelForm):
#     '''
#     Class that handles comments
#     '''
#     class Meta:
#         model = Comments
#         fields = "__all__"
#         exclude = ["pub_date"]


