from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='media/', blank=True, null=True)
    about_me = models.TextField(blank=True)


    @property
    def github_profile_url(self):
        return f"https://github.com/{self.github_link}"

    def __str__(self):
        return self.user.username + "'s Profile"


