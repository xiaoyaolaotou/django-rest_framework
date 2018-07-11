from django.shortcuts import render
from rest_framework import viewsets
from .models import ProductModel,Manufacturer
from .serializers import ManufacturerSerializers,ProductModelSerializers



class ManufacturerViewset(viewsets.ModelViewSet):
    """
    Retrieve:
        返回单个制造商信息
    List:
        返回制造商例表
    update:
        更新制造商信息
    destroy:
        删除制造商记录
    create:
        创建制造商记录
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializers
    lookup_field = "id"


class ProductModelViewset(viewsets.ModelViewSet):
    """
    Retrieve:
        返回单个产品型号信息
    List:
        返回产品型号例表
    update:
        更新产品型号信息
    destroy:
        删除产品型号记录
    create:
        创建产品型号记录
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializers
    lookup_field = "id"