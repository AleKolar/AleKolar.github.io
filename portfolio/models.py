from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_link = models.URLField(max_length=200, default='https://github.com/dashboard')
    photo = models.ImageField(upload_to='profile_photos/', default='profile_photos/default.jpg')

    @property
    def github_profile_url(self):
        return f"https://github.com/{self.github_link}"

    def __str__(self):
        return self.user.username + "'s Profile"


