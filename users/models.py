from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    # Too bad I am deploying on Heroku
    email = models.EmailField(blank=True, null=True)


    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.user.pk})