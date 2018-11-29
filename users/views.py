from django.shortcuts import render
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy
# Create your views here.


class UserSignupView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"