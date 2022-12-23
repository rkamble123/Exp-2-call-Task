from django.shortcuts import render
from django.views import View
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from . models import CourseModel,TopicsModel
from .serializers import CourseSerializer,TopicSerializer
from .MyPermissions import MyPermission
# Create your views here.


# User Model Views

class LCUser_api(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes= [MyPermission]

    # To Get Existing Users Data

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # To Create New User

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)



class RUDUser_api(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes= [MyPermission]
    
    # To Retrive Perticular Users Data 

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    # To Update Perticular Users Data

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # To Delete Perticular User

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)






# Course Model Views


class LCCourse_api(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]

    # To Get Existing Course Data

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # To Create New Course

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)



class RUDCourse_api(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    
    # To Retrive Perticular Course Data 

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    # To Update Perticular Course Data

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # To Delete Perticular Course

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)




# Topic Model Views


class LCTopics_api(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = TopicsModel.objects.all()
    serializer_class = TopicSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]

    # To Get Existing Topic Model Data

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    # To Create New Topic

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)



class RUDTopics_api(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = TopicsModel.objects.all()
    serializer_class = TopicSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    
    # To Retrive Perticular Topic information

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)

    # To Update Perticular Topic Data

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    # To Delete Perticular Topic

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args,**kwargs)