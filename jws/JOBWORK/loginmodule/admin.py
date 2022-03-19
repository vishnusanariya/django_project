from django.contrib import admin

# Register your models here.
from .models import regis
from .models import Profile
admin.site.register(regis)
admin.site.register(Profile)