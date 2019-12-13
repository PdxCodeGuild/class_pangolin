from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
    form_class= UserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'signup.html'
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class UserProfileView(generic.DeleteView):
    model = User
    template_name = 'user_profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

# Create your views here.
