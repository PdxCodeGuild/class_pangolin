from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, filters
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status

from .models import Ticket
from .serializers import TicketSerializer, UserSerializer, FileSerializer

def index(request):
    return render(request, 'bug_me_app/index.html', {})

def logout_request(request):
    logout(request)
    return redirect('bug_me_app:index')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid')
        else:
                messages.error(request, 'Invalid')
    form = AuthenticationForm()
    return render(request = request, template_name = 'bug_me_app/login.html', context={'form':form})

class TicketList(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['search']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['search']
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FileUploadView(APIView):
    parser_classes = (FileUploadParser, MultiPartParser, FormParser)

    def put(self, request, format=None):
        if 'file' not in request.data:
            raise ParseError('Empty Content')

        f = request.data['file']

        Ticket.file.save(f.name, f, save=True)
        return Response(status=status.HTTP_201_CREATED)

        # file_serializer = FileSerializer(data=request.data)

        # if file_serializer.is_valid():
        #     file_serializer.save()
        #     return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(file_serializer.error, status=status.HTTP_400_BAD_REQUEST)

            
