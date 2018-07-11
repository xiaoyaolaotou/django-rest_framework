from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CabinetSerializer
from .models import Cabinet

class CabinetViewset(viewsets.ModelViewSet):
    """
    Retrieve:
        返回单个机柜信息
    List:
        返回机柜例表
    update:
        更新机柜信息
    destroy:
        删除机柜记录
    create:
        创建机柜记录
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    lookup_field = "id"