from django.shortcuts import render
from .models import employclass
from rest_framework import generics
from .serializers import employserializer
class employlist(generics.ListCreateAPIView):
                   queryset=employclass.objects.all()
                   serializer_class=employserializer
class employdel(generics.RetrieveUpdateDestroyAPIView):
                   queryset=employclass.objects.all()
                   serializer_class=employserializer