import os
from django.test import TestCase
from django.contrib.auth.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_prj.settings')
import django
django.setup()

# Create your tests here.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_prj.settings')
import django
django.setup()

from .models import Post
from users_app.models import Profile


# Create your tests here.
class PostTestsClass(TestCase):
    def setUp(self):
        self.profile_test = Profile( user=User(name='Joe',username='Joe'))
        self.profile_test.save()

        self.post_test = Post(id=1, caption="Greenery",image="default.png",likes=0,comments="comment test", hashtags="#nature", user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.post_test, Post))

    def test_save_image(self):
        self.post_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)
