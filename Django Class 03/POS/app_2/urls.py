from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import Usermvc

router = DefaultRouter()
router.register("user", Usermvc, "user")

urlpatterns = [] + router.urls