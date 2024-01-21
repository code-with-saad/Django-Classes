from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import mixins
from rest_framework.response import Response
from app_1.serializers import PersonSerializer
from app_1.models import PersonModel

# Create your views here.


# APIView
# Generics
# Viewset - restfull guidelinces



persons = [
    {
        "id": 1,
        "name": "Saad"
    },
    {
        "id": 2,
        "name": "Ahmed"
    }
]

@api_view(["GET"])
def get_persons(request):
    return Response(persons)


@api_view(["GET"])
def get_persons_from_db(request: Request):
    persons_db = PersonModel.objects.all()
    serialized_person = PersonSerializer(persons_db, many=True)
    return Response(serialized_person.data)


class PersonModelViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = PersonModel.objects.all()



# class PersonViewSet(ViewSet):
#     pass