from rest_framework import generics

from .models import Pet
from .serializers import PetSerializer


class ListPet(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class DetailPet(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
