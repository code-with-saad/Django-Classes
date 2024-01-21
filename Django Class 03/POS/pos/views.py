from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

class UserMVS(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        username = data["username"]
        password = data["password"]
        # is_staff=1
        # is_superuser=1

        user = User.objects.create(
            username = username,
            password = password,
            is_staff=1,
            is_superuser=1
        )

        serialiezed_user = self.serializer_class(user)

        # serialiezed_user = self.serializer_class(data=data)
        # if serialiezed_user.is_valid():
        #     user = serialiezed_user.save()

        user.set_password(password)
        user.save()

        return Response(serialiezed_user.data)
        
    
