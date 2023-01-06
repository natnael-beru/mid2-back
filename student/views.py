from django.shortcuts import render


from django.shortcuts import render
from .models import studentclass
from rest_framework import generics
from .serializers import studentserializer
class studentlist(generics.ListCreateAPIView):
                   queryset=studentclass.objects.all()
                   serializer_class=studentserializer
class studentdel(generics.RetrieveUpdateDestroyAPIView):
                   queryset=studentclass.objects.all()
                   serializer_class=studentserializer
