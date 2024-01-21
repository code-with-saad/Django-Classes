from rest_framework.routers import DefaultRouter
from . views import BlogModelViewSet

router = DefaultRouter()
router.register("blog", BlogModelViewSet, 'blog')

urlpatterns = [] + router.urls