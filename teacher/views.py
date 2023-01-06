from django.shortcuts import render


from django.shortcuts import render
from .models import techclass
from rest_framework import generics
from .serializers import teserializer
class techlist(generics.ListCreateAPIView):
                   queryset=techclass.objects.all()
                   serializer_class=teserializer
class techdel(generics.RetrieveUpdateDestroyAPIView):
                   queryset=techclass.objects.all()
                   serializer_class=teserializer
