from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.
def users(request):
  return render(request, 'users/users.html')

def user_registration(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f" {username}, Your account was successfully created!")
      return redirect('login')
  else:
    form = UserRegistrationForm()
  return render(request, 'users/registration.html', {'form': form})
