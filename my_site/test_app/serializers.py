from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Member


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Member
        fields = ('user', 'gender', 'country')

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        gender = validated_data.pop('gender')
        country = validated_data.pop('country')
        member = Member()
        user = User.objects.create_user(username, password)
        member.user = user
        member.gender = gender
        member.country = country
        return member

