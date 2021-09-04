from django.shortcuts import render
from .serializers import  SearchSerializer
from rest_framework.generics import ListAPIView
from AUTH.models import AuthUser
# Create your views here.
class SearchView(ListAPIView):
    serializer_class=SearchSerializer

    def queryset(self):
        username=self.request.data.get('username',None)
        if username is not None:
            return AuthUser.objects.all().filter(username=username)
        return 
