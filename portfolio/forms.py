

from django import forms
from .models import Profile, Achievements


class CreateProfileForm(forms.ModelForm):
    photo = forms.ImageField(label='Profile Photo')

    class Meta:
        model = Profile
        fields = ['github_link', 'photo', 'about_me']

class CreateAchievementsForm(forms.ModelForm):
    certificates = forms.ImageField(label='Certificates')

    class Meta:
        model = Achievements
        fields = ['name', 'achievements', 'skills', 'certificates']