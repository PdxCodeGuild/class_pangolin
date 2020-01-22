from django.shortcuts import render


def index(request):
    return render(request, 'fetch/index.html', {'title': 'Index'})


def home(request):
    # context = {
    #     'pets': Pet.objects.all()
    # }
    return render(request, 'fetch/home.html')


def about(request):
    return render(request, 'fetch/about.html', {'title': 'About'})


def register(request):
    return render(request, 'fetch/register.html', {'title': 'Register'})
