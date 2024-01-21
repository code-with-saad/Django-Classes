from rest_framework import serializers
from .models import BlogModel
from account.serializers import User2Serializer
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
    author = User2Serializer()
    class Meta:
        model = BlogModel
        fields = "__all__"
        # depth = 1

class BlogPostSerializer(serializers.ModelSerializer):
    # author = serializers.ChoiceField(choices=User.objects.filter(id=2).values_list('id', 'username'))
    class Meta:
        model = BlogModel
        fields = "__all__"