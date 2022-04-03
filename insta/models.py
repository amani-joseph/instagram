from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    caption = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    likes = models.BigIntegerField(default=0)
    comments = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hashtags = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

