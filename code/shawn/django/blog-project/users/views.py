from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # no need to input model since UserCreationForm knows how to get model already
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserProfileView(generic.DetailView):
    model = User 
    template_name = 'user_profile.html'

    # since we are using the username to lookup a user, instead of pk, we need to create our own get_object
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])    # 'username" is what's specfified in the urlconf

