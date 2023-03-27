from abc import ABC

from rest_framework import serializers
from .models import Category, Channel, Favorites, Users





class ChannelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    channels = ChannelModelSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'channels']



class FavoriteModelSerializer(serializers.ModelSerializer):
    channel = ChannelModelSerializer(many=False)
    class Meta:
        model = Favorites
        fields = ['channel']

class UsersModelSerializer(serializers.ModelSerializer):
    favorite = FavoriteModelSerializer(many=True)

    class Meta:
        model = Users
        fields = ['user','favorite']
