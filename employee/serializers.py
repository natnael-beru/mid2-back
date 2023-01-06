from rest_framework import serializers
from .models import employclass
class employserializer(serializers.ModelSerializer):
            class Meta: 
                    model=employclass
                    fields='__all__'
    
     