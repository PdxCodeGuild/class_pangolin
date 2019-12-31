from django.shortcuts import render

def Make(request):
    return render(request, 'home.html')