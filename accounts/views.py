from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError
# from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, LoginSerializer
from .models import CustomUser

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            access_token = str(AccessToken.for_user(user))
            refresh_token = str(RefreshToken.for_user(user))
            return Response({"message": "User registered successfully", "access_token": access_token,
                             "refresh_token": refresh_token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            access_token = str(AccessToken.for_user(user))
            refresh_token = str(RefreshToken.for_user(user))
            return Response({"access_token": access_token,
                             "refresh_token": refresh_token}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response("Logout Successful", status=status.HTTP_200_OK)
        except TokenError:
            return Response({"message": "Invalid Token"}, status=status.HTTP_400_BAD_REQUEST)
    
class UserRetrieve(APIView):
    """ Get Particular user detail """
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        user = request.user
        serializer = UserSerializer(instance=user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)