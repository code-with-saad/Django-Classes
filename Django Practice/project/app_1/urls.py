from django.urls import path
from . import views


urlpatterns = [
    # static data 
    path("static/list", views.get_static_data),

    # data from db
    path("dynamic/list", views.get_dynamic_data)
]