from rest_framework import serializers
from .models import *





class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personage
        fields = ['age', 'money', 'items',
                  'status', 'date', 'dateToTrack',
                  'happy_level', 'eat_level', 'health_level', 'house', 'transport']




class UserSerializer(serializers.ModelSerializer):
    Character = CharacterSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['Id', 'Username', 'Firstname', 'LastName', 'Character']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.save()
        return user
