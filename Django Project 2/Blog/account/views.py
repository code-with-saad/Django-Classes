from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

class RegisterAPIView(APIView):
    def post(self, request: Request):
        serialized_data = UserSerializer(data=request.data)
        if serialized_data.is_valid():
            user: User = serialized_data.save()
            user.set_password(request.data["password"])
            user.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    def post(self, request: Request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username is None or password is None:
            return Response({
                "error": "Please fill out all fields"
            }), status.HTTP_400_BAD_REQUEST
        user = User.objects.filter(username=username).first()
        if user is None:
            return Response({
                "error": "User does not exist"
            }), status.HTTP_400_BAD_REQUEST
        is_auth_user = authenticate(username=username, password=password)
        if is_auth_user is None:
            return Response({
                "error": "Wrong Credentials"
            })
        login(user=user, request=request)
        return Response({
            "message": "User Logged in successfully"
        })
    
class LogoutAPIView(APIView):
    def logout(self, request):
        logout(request)
        return Response({"message": "Successfully Logged out"})
