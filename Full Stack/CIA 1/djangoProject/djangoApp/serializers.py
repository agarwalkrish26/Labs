from rest_framework import serializer

from .models import APIModel

class APIserializer(serializer.HyperlinkedModelSerializer):
    
    class Meta:
        model=APIModel
        fields=("title", "description")