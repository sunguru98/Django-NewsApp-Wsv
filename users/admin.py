from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CutomUserCreationForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CutomUserCreationForm
    form = CustomUserChangeForm
    list_display = ["username", "email", "user_age"]
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)