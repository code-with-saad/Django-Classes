from django.urls import path
from . import views

urlpatterns =[
    path("", views.get_all_persons),
    path("params/<id>", views.get_person_by_path_params),
    path("query", views.get_person_by_query_str),
    path("add_person", views.add_persons),
]