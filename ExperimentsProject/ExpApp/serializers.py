from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CourseModel,TopicsModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicsModel
        fields = "__all__"