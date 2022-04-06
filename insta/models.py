from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
# from users_app.models import Profile

# Create your models here.

# class Comments(models.Model):
    


class Post(models.Model):
    # name = models.CharField(max_length=200, null=True, blank=True)
    caption = models.CharField(max_length=200, null=False, unique=True, blank=True)
    image = CloudinaryField('posts/', null=False, blank=False )
    likes = models.BigIntegerField(default=0)
    comments = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtags = models.CharField(max_length=200, null=False,default='#', blank=True)

    def __str__(self):
        return self.caption
    
    def save_post(self):
        self.save()
    
    def get_absolute_url(self):
        return reverse('insta-home')


# class Comment(models.Model):
#     comment = models.TextField()
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
#     created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return f'{self.user.name} Post'

#     class Meta:
#         ordering = ["-pk"]