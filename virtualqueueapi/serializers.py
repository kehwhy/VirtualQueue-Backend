from rest_framework import serializers

from .models import User, Line

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'