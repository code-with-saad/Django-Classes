from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from django.contrib.auth import login, logout, authenticate
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission



# Create your views here.

class PublicPermisson(BasePermission):
    def has_permission(self, request, view):
        return True


class Usermvc(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["POST"], permission_classes= [PublicPermisson])
    def login(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user= User.objects.filter(username=username).first()

        if user is None:
            return Response({"error": "User not found"})

        is_valid_user = authenticate(username=username, password=password)

        if is_valid_user is None:
            return Response({"error": "Wrong Credentials"})
        
        login(user=user, request=request)

        return Response({"message": "Login successful"})
    
    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        return Response({"message": "Successfully Logged out"})
    
    def get_queryset(self):
        print(self.request.user.id)
        user_id = self.request.user.id
        return User.objects.filter(id=user_id).all()

    @action(detail=False, methods=['get'])
    def test_1(self, request: Request):
        print(request.user)
        return Response({"message": "Test_1"})