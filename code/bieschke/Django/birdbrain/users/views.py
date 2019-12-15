from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

class UserSignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login') 
    template_name = 'profile_create.html'

class UserProfileView(generic.DetailView):
    model = User
    template_name = 'profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
        