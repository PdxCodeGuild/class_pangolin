from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import DetailView, CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Profile
from .forms import FollowForm
from posts.models import Chirp

class UserProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

    # get username string
    def get_object(self):
        this_user = get_object_or_404(User, username=self.kwargs['username'])   # get the user
        return this_user.profile

class UserSignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'profile_edit.html'

    fields = ['first_name', 'last_name', 'headline', 'summary', 'location', 'picture']

    def test_func(self):
        # get the profile
        obj = self.get_object()
        # make sure logged in user (self.request.user) is the same as the profile owner (obj.author)
        return self.request.user == obj.user


# for getting login required to work for a functional view, add decorator @login-required before the function
class FollowProfileView(LoginRequiredMixin, FormView):
    template_name = 'base.html'
    success_url = reverse_lazy('posts:home')
    form_class = FollowForm

    def form_valid(self,form):
        # user1 is logged in user
        user1 = self.request.user
        # user2 is who use1 wants to follow
        user2 = User.objects.get(username=form.cleaned_data['username'])
        print(f"user1 is {user1} user2 is {user2}")
        # add as many-to-many in db
        user1.profile.users_followed.add(user2.profile)

        return super().form_valid(form)


class UnfollowProfileView(LoginRequiredMixin, UpdateView):
    model = Profile