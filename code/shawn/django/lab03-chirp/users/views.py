from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Profile
from posts.models import Chirp

class UserProfileView(DetailView):
    model = User
    # context_object_list = Chirp.objects.filter(author=)
    template_name = 'profile.html'

    # get username string
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

class UserSignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile_edit.html'

    fields = ['first_name', 'last_name', 'headline', 'summary', 'location', 'picture']

    # def test_func(self):
    #     # get the profile
    #     obj = self.get_object()
    #     # make sure logged in user (self.request.user) is the same as the profile owner (obj.author)
    #     return self.request.user == obj.user
