from rest_framework import serializers
from .models import Cap

class CapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cap
        fields = '__all__'