from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import AuthUser

User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password', 'token']


    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return str(token)


