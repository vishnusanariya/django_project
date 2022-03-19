from django.contrib import admin

# Register your models here.
from .models import deal, jobs,History
admin.site.register(jobs)
admin.site.register(History)
admin.site.register(deal)