from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import UserModel
from .serializers import UserSerializer

# Create your views here.

persons = [
    {
        "id": 1,
        "name": "saad"
    },
    {
        "id": 2,
        "name": "ahmed"
    },
    {
        "id": 3,
        "name": "ali"
    },
    {
        "id": 4,
        "name": "rafay"
    },

]


# -------------------------------- Static Data --------------------------------

@api_view(["GET"])
def get_static_data(request):
    return Response(persons)




# -------------------------------- Data from DB --------------------------------


@api_view(["GET"])
def get_dynamic_data(request):
    data = UserModel.objects.all()
    serialized_data = UserSerializer(data, many=True)
    return Response(serialized_data.data)


@api_view(["POST"])
def add_dynamic_data(request):
    pass
