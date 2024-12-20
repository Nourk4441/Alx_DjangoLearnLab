from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

   # Use the custom user model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {
            'followers': {'read_only': True},
        }

    def create(self, validated_data):
        # Create the user with the provided password
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user
