from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from .models import AuthUser
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import SignupSerializer
from rest_framework.generics import CreateAPIView

User = get_user_model()


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        token, created = Token.objects.get_or_create(user_id=response.data["id"])
        response.data["token"] = str(token)
        return response


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email='email', password=password)

        if user is not None:
            context = {'token': str(Token.objects.get(user=user))}
            return Response(data=context, status=status.HTTP_200_OK)

        else:
            context = {'message': str('invalid credential')}
            return Response(data=context, status=status.HTTP_401_UNAUTHORIZED)
