from rest_framework import serializers
from .models import User, UserProfile

class UserProfileSerializer(serializers.Serializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create_user(**validated_data)
