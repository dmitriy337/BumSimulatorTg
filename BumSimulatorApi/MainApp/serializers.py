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


class EatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eat_activity
        fields = ['id', 'name', 'description', 'price',
                  'howMuchHealthMin', 'howMuchHealthMax',
                  'howMuchEatMin', 'howMuchEatMax',
                  'howMuchHappyMin', 'howMuchHappyMax']


class HappySerializer(serializers.ModelSerializer):
    class Meta:
        model = Happy_activity
        fields = ['id', 'name', 'description', 'price',
                  'howMuchHealthMin', 'howMuchHealthMax',
                  'howMuchEatMin', 'howMuchEatMax',
                  'howMuchHappyMin', 'howMuchHappyMax']


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Health_activity
        fields = ['id', 'name', 'description', 'price',
                  'howMuchHealthMin', 'howMuchHealthMax',
                  'howMuchEatMin', 'howMuchEatMax',
                  'howMuchHappyMin', 'howMuchHappyMax']


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Houses
        fields = ['id', 'name', 'description', 'price',
                  'howMuchRating', 'unlockRating']


class LearningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Learning_params
        fields = ['id', 'name', 'description', 'price',
                  'howMuchRating', 'unlockRating']


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transports
        fields = ['id', 'name', 'description', 'price',
                  'howMuchRating', 'unlockRating']
