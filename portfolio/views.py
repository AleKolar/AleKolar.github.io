from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Profile, Achievements
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile
from .forms import CreateProfileForm, CreateAchievementsForm
from django.contrib.auth.views import LoginView

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/accounts/profile/'

def profile_view(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


class CreateProfileView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'create_profile.html'
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        profile_exists = Profile.objects.filter(user=self.request.user).exists()
        if profile_exists:
            profile = Profile.objects.get(user=self.request.user)
            form.instance.user = self.request.user
            form.instance.photo = form.cleaned_data.get('photo')
            form.instance.about_me = form.cleaned_data.get('about_me')
            form.instance.save()
        else:
            form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'update_profile.html'
    success_url = '/accounts/profile/'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.photo = form.cleaned_data.get('photo')
        form.instance.save()
        return super().form_valid(form)


class CreateAchievementsView(LoginRequiredMixin, CreateView):
    model = Achievements
    form_class = CreateAchievementsForm
    template_name = 'create_achievements.html'

    def form_valid(self, form):
        profile = self.request.user.profile
        form.instance.name = profile
        form.instance.achievements = form.cleaned_data['achievements']
        form.instance.certificates = form.cleaned_data.get('certificates')
        if 'certificates' in self.request.FILES:
            form.instance.certificates = self.request.FILES['media']
        if 'skills' in form.cleaned_data:
            form.instance.skills = form.cleaned_data['skills']
        form.instance.save()

        return redirect('achievements')

    def get_success_url(self):
        return reverse('achievements')

def achievements_view(request):
    achievements = Achievements.objects.all()
    context = {
        'achievements': achievements,
    }
    return render(request, 'achievements.html', context)

class UpdateAchievementsView(LoginRequiredMixin, UpdateView):
    model = Achievements
    form_class = CreateAchievementsForm
    template_name = 'update_achievements.html'
    success_url = reverse_lazy('achievements')

    def get_object(self, queryset=None):
        return Achievements.objects.get(pk=self.kwargs['pk'])

    def form_valid(self, form):
        profile = self.request.user.profile
        form.instance.name = profile
        form.instance.achievements = form.cleaned_data['achievements']
        form.instance.certificates = form.cleaned_data.get('certificates')
        if 'media' in self.request.FILES:
            form.instance.certificates = self.request.FILES['media']
        if 'skills' in form.cleaned_data:
            form.instance.skills = form.cleaned_data['skills']
        form.instance.save()

        return super().form_valid(form)

