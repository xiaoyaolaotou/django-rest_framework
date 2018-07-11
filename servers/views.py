from django.shortcuts import render
from rest_framework import viewsets,mixins
from .serializers import ServerAutoReportSerializer,IPSerializer,NetworkDeviceSerializer,ServerSerializer
from .models import *
from ops.permissions import Permission
class ServerAutoReportViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """
    create:
        创建服务器记录
    """
    queryset = Server.objects.all()
    serializer_class = ServerAutoReportSerializer


class ServerViewset(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve:
        返回单个服务器信息
    List:
        返回服务器例表

    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = "id"


class NetworkDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve:
        返回单个网卡信息
    List:
        返回网卡例表

    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer
    lookup_field = "id"


class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    Retrieve:
        返回单个IP信息
    List:
        返回IP例表

    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer
    lookup_field = "id"

