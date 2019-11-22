from django.contrib.auth.models import User, Group
from rest_framework import serializers


class User_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'group']

class Group_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
