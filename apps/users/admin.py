from django.contrib import admin

# Register your models here.

from .models import UserProject

class UserprofileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProject,UserprofileAdmin)