from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from .models import AuthUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import SignupSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
#it is view
User = get_user_model()


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()



class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        
        if user is not None:
            context = {'token': str(Token.objects.get(user=user))}
            return Response(data=context, status=status.HTTP_200_OK)

        else:
            context = {'message': str('invalid credentials')}
            return Response(data=context, status=status.HTTP_401_UNAUTHORIZED)
