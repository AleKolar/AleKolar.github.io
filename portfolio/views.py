from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile
from .forms import CreateProfileForm
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
            form.instance = profile
            form.instance.user = self.request.user
            # form.instance.photo = form.cleaned_data['media']
            form.instance.photo = self.request.FILES['media']
            form.instance.about_me = form.cleaned_data['about_me']
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
        return super().form_valid(form)

