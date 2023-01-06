from rest_framework import serializers
from .models import techclass
class teserializer(serializers.ModelSerializer):
           class Meta:
                    model=techclass
                    fields='__all__'