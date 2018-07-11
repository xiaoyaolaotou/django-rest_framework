from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import CursorPagination
from django_filters.rest_framework import DjangoFilterBackend
User = get_user_model()
from .filters import UsersFilter
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from ops.permissions import Permission
from rest_framework import permissions



class UserViewset(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve:
        返回单个用户信息
    List:
        返回用户例表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


    filter_backends = (DjangoFilterBackend,)#使用djangofilter做为搜索后端
    #filter_fields = ("email",) #精准匹配，使用哪个字段作为搜索条件
    filter_class = UsersFilter
    extra_perm_map = {
        #"GET":['%(app_label)s.add_%(model_name)s']
        "GET":['auth.view_user'],
    }


    #添加认证信处
    #authentication_classes = (SessionAuthentication,)
    #添加登录权限

    # extra_perm_map = {
    #     "GET":['auth.view_user']
    # }
