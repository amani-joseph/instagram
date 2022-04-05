from django.urls import path
from .views import (
    PostListView,
    # PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='insta-home'),
    # path('', views.index, name='insta-home'),
    ]
