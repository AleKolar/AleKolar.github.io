from django.contrib import admin
from .models import Profile

if admin.site.is_registered(Profile):

    admin.site.unregister(Profile)

admin.site.register(Profile)

