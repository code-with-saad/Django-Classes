from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from HRMS.models import Person
from HRMS.serializers import PersonSerializer
import json

persons = [
    {
        "id": 1,
        "name": "Saad",
    },
    {
        "id": 2,
        "name": "Ali"
    }
]


@api_view(["GET"])
def get_all_persons(request: HttpRequest):
    # persons = Person.objects.all()
    # person_searializer = PersonSerializer(persons, many=True)
    if request.method == "GET":
        return Response(persons)
    

@api_view(["GET"])
def get_person_by_path_params(request: HttpRequest, id):
    if request.method == "GET":
        for user_id in persons:
            if int(id) == user_id["id"]:
                return Response(user_id)
    return Response("Not found")


@api_view(["GET"])
def get_person_by_query_str(request: HttpRequest):
    if request.method == "GET":
        data = request.GET.get("id")
        for value in persons:
            if value["id"] == int(data):
                return Response(value)
    return Response("Not found")


@api_view(["POST"])
def add_persons(request: HttpRequest):
    data = json.loads(request.body)
    print("data added")
    # for user in persons:
    persons.append(data)
    return Response(persons)


# --------- Get ---------
# query_string
# path_parameter
# --------- Post ---------
# Json
# --------- 
# query_string
# request.get.items()
# ---------
# path_parameter
# request.
# ---------
# json
# import json
# json.loads(request.body)





































