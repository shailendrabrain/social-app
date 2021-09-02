from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import AuthUser

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        def create(self, validated_data):
            # user = User.objects.create(
            #     username=validated_data['username'],
            #     first_name=validated_data['first_name'],
            #     last_name=validated_data['last_name'],
            #     email=validated_data['email'],
            # )

            user = User.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            Token.objects.create(user=user)
            return user
