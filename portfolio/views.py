from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
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
    success_url = 'profile.html/'

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
    success_url = '/success/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
