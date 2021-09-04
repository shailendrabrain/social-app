from rest_framework.serializers import ModelSerializer
from AUTH.models import AuthUser


class SearchSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username','profile_photo','first_name','last_name']