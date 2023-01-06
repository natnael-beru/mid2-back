from rest_framework import serializers
from .models import studentclass
class studentserializer(serializers.ModelSerializer):
                class Meta:
                    model=stuclass
                    fields='__all__'
