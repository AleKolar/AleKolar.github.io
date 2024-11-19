from django.urls import path
from .views import profile_view, CreateProfileView, CustomLoginView, register_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
]