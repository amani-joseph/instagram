from django.urls import path
from .views import (
    PostListView,
    AuthorDetailView,
    PostCreateView,
    # PostUpdateView,
    # PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='insta-home'),
    path('user/<int:pk>/', AuthorDetailView.as_view(), name='author-profile'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    # path('post/new/', views.PostCreate, name='post_create'),
    # path('', views.index, name='insta-home'),
    ]


# PostCreate