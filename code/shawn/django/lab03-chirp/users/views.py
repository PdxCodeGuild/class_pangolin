from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import DetailView, CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
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

   #auto login after register: 
    def form_valid(self, form):
        #save the new user first
        form.save()
        #get the username and password
        username = self.request.POST['username']
        password = self.request.POST['password1']
        #authenticate user then login
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
        login(self.request, user)
        return HttpResponseRedirect(reverse('posts:home'))


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'profile_edit.html'

    fields = ['first_name', 'last_name', 'headline', 'summary', 'location', 'picture']

    def test_func(self):
        # get the profile
        obj = self.get_object()
        # make sure logged in user (self.request.user) is the same as the profile owner (obj.author)
        return self.request.user == obj.user

@login_required
def follow(request):
    # user1 is logged in user
    user1 = request.user
    # user2 is who use1 wants to follow
    user2 = User.objects.get(username=request.POST['username'])
    # add as many-to-many in db
    user2.profile.users_followed.add(user1.profile)

    return HttpResponseRedirect(reverse('users:profile', args=(request.POST['username'],)))

@login_required
def unfollow(request):
    # person to unfollow
    person_to_unfollow = User.objects.get(username=request.POST['username'])
    # remove their profile from friends list
    link_to_delete = request.user.profile.friends.remove(person_to_unfollow.profile)

    return HttpResponseRedirect(reverse('users:profile', args=(request.POST['username'],)))
