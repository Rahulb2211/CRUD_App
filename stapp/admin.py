from django.contrib import admin

# Register your models here.
from .models import profile

admin.site.register(profile)
class profileAdmin(admin.ModelAdmin): 
    list_display = ('id', 'name', 'email', 'password', 'marks')
# @admin.register(profile)
# class profileAdmin(admin.ModelAdmin()
#     list_display = ("id", "name", "email", "password")
