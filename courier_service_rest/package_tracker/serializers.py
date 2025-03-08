from rest_framework import serializers
from .models import Package


class PackageSerializer(serializers.ModelSerializer):
#PackageSerializer is a class that inherits from serializers.ModelSerializer
    class Meta:
        model = Package
        fields = '__all__'