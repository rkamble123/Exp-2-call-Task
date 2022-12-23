from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
urlpatterns = [

    path("auth/",include('rest_framework.urls',namespace='rest_framework')),
    # path("gettoken/",obtain_auth_token),
    path('get_token/',TokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('refresh_token/',TokenRefreshView.as_view(),name="token_refresh"),
    path("verify_token/",TokenVerifyView.as_view(),name='verify_token'),


    # User Model Access Urls

    path("LCUser_api/",views.LCUser_api.as_view(),name = 'LCUser_api'),
    path("RUDUser_api/<int:pk>",views.RUDUser_api.as_view(),name = 'RUDUser_api'),


    # Course Model Access Urls

    path("LCCourse_api/",views.LCCourse_api.as_view(),name = 'LCCourse_api'),
    path("RUDCourse_api/<int:pk>",views.RUDCourse_api.as_view(),name = 'RUDCourse_api'),


    # Topic Model Access Urls

    path("LCTopics_api/",views.LCTopics_api.as_view(),name = 'LCTopics_api'),
    path("RUDTopics_api/<int:pk>",views.RUDTopics_api.as_view(),name = 'RUDTopics_api'),

]