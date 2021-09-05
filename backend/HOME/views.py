from django.shortcuts import render
from .serializers import SearchSerializer
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

User = get_user_model()

class SearchView(ListAPIView):
    serializer_class = SearchSerializer

    def get_queryset(self):
        username = self.request.data.get('username', '')
        print(username)
        return User.objects.filter(username__icontains=username)