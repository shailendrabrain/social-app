from django.shortcuts import render
from .serializers import  SearchSerializer
from rest_framework.generics import ListAPIView
from AUTH.models import AuthUser


class SearchView(ListAPIView):
    serializer_class=SearchSerializer

    def get_queryset(self):
        data=self.get_object()
        print(data)
        username=self.request.data.get('username', None)
        print("input username",username)
        if username is not None:
            return AuthUser.objects.all().filter(username=username)
        return 
