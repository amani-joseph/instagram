from email.mime import image
from django.test import TestCase
from .models import Profile, Post
from django.contrib.auth.models import User
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_prj.settings')
import django
django.setup()
# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Joe')
        self.user.save()

        self.profile_test = Profile(id=1,  image='default.png', bio='I really dont like tests', user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

