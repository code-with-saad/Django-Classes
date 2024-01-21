from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import BlogModel
from .serializers import BlogSerializer, BlogPostSerializer

class BlogModelViewSet(ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogPostSerializer


    def get_queryset(self, *args, **kwargs):
        return BlogModel.objects.filter(author_id=self.request.user.id).all()

    
    def __init__(self, *args, **kwargs):
        super(BlogModelViewSet, self).__init__(*args, **kwargs)
        self.serializer_action_classes = {
        'list': BlogSerializer,
        'create':BlogPostSerializer,
        'retrieve':BlogSerializer,
        'update':BlogPostSerializer,
        'partial_update':BlogPostSerializer,
        'destroy':BlogPostSerializer,
        }


    def get_serializer_class(self, *args, **kwargs):
        kwargs['partial'] = True
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(BlogModelViewSet, self).get_serializer_class()

