from django.urls import path
from . import views
from .views import PersonModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "mvs", PersonModelViewSet
)

urlpatterns = [
    path("list", views.get_persons),
    path("list_db", views.get_persons_from_db),
] + router.urls