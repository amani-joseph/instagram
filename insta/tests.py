import os
from django.test import TestCase

# Create your tests here.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_prj.settings')
import django
django.setup()

from .models import Post


# Create your tests here.
class PostTestsClass(TestCase):
    # set up method
    def setUp(self):
        self.post = Post.objects.create(caption="Greenery",image="",likes=0,comments="" pub_date="",user="Amani", hashtags="#nature")

    # testing instance
    def test_instance(self):
        post = self.post
        self.assertEqual(self.post, post)

    # testing save method
    def test_save_post_method(self):
        self.post.save_location()
        post = Post.objects.all()
        self.assertTrue(len(Post) > 0)

