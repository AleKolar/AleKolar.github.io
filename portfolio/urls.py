from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import profile_view, CreateProfileView, CustomLoginView, register_view, UpdateProfileView, \
    CreateAchievementsView, achievements_view, UpdateAchievementsView

urlpatterns = [
    path('', profile_view, name='profile'),
    path('accounts/profile/', profile_view, name='profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create_profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', register_view, name='register'),
    path('update/', UpdateProfileView.as_view(), name='update_profile'),
    path('create_achievements/', CreateAchievementsView.as_view(), name='create_achievements'),
    path('achievements/', achievements_view, name='achievements'),
    path('accounts/achievements/', achievements_view, name='achievements'),
    path('accounts/create_achievements/', CreateAchievementsView.as_view(), name='create_achievements'),
    path('achievements/<int:pk>/update/', UpdateAchievementsView.as_view(), name='update_achievements'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)