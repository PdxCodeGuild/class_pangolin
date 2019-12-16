from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Chirp, Comment 

class ChirpHomeView(ListView):
    model = Chirp
    template_name = 'home.html'

class FeedView(ListView):
    model = Chirp
    template_name = 'home_filtered.html'

class ChirpCreateView(LoginRequiredMixin, CreateView):
    model = Chirp
    template_name = 'create.html'

    fields = ['text', 'picture']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ChirpEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chirp
    template_name = 'edit.html'

    fields = ['text', 'picture']

    def test_func(self):
        # get the chirp
        obj = self.get_object()
        # make sure logged in user (self.request.user) is the same as the author (obj.author)
        return self.request.user == obj.author

class ChirpDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chirp
    template_name = "delete.html"
    success_url = reverse_lazy('posts:home') # must give DeleteView a URL to redirect to once successful

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

class ChirpDetailView(DetailView):
    model = Chirp
    template_name = 'chirp.html'

@login_required
def like(request):

    # figure out who the liker is
    liker = request.user
    # figure out post to be liked
    chirp_to_be_liked = Chirp.objects.get(id=request.POST['chirp_id'])

    # if the like already exists, otherwise add one
    if chirp_to_be_liked in liker.profile.chirps_liked.all():
        # remove it
        liker.profile.chirps_liked.remove(chirp_to_be_liked)
    else:  
        # create many-to-many like link in DB
        liker.profile.chirps_liked.add(chirp_to_be_liked)
        # remove dislike and remove if necessary
        liker.profile.chirps_disliked.remove(chirp_to_be_liked)

    return HttpResponseRedirect(reverse('posts:home'))

@login_required
def dislike(request):

    # figure out who the disliker is
    disliker = request.user
    # figure out post to be disliked
    chirp_to_be_disliked = Chirp.objects.get(id=request.POST['chirp_id'])

    # if the like already exists
    if chirp_to_be_disliked in disliker.profile.chirps_disliked.all():
        # remove it
        disliker.profile.chirps_disliked.remove(chirp_to_be_disliked)

    else:
        # create many-to-many link in DB
        disliker.profile.chirps_disliked.add(chirp_to_be_disliked)
        # remove like if necessary
        disliker.profile.chirps_liked.remove(chirp_to_be_disliked)
    
    return HttpResponseRedirect(reverse('posts:home'))

# for reference, from following
# @login_required
# def follow(request):
#     # user1 is logged in user
#     user1 = request.user
#     # user2 is who use1 wants to follow
#     user2 = User.objects.get(username=request.POST['username'])
#     # add as many-to-many in db
#     user2.profile.users_followed.add(user1.profile)

#     return HttpResponseRedirect(reverse('users:profile', args=(request.POST['username'],)))

# @login_required
# def unfollow(request):
#     # person to unfollow
#     person_to_unfollow = User.objects.get(username=request.POST['username'])
#     # remove their profile from friends list
#     link_to_delete = request.user.profile.friends.remove(person_to_unfollow.profile)

#     return HttpResponseRedirect(reverse('users:profile', args=(request.POST['username'],)))