from django.shortcuts import render, redirect
from .forms import UsersForm
from .models import Users
from django.views.generic import CreateView

class NewCreateView(CreateView):
    model = Users
    template_name = 'registration/create_user.html'
    form_class = UsersForm