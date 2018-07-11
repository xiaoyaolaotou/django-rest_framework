from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Idc
from .serializers import IdcSerializer


class IdcList(APIView):
    def get(self,request):
        """获取所有数据"""
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        """创建数据"""
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class IdcDetail(APIView):

    def get(self,request,id):
        """获取某一条数据"""
        idc = Idc.objects.get(id=id)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self,request,id):
        """更新某一条数据"""
        idc = Idc.objects.get(id=id)
        serializer = IdcSerializer(idc,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,id):
        idc = Idc.objects.get(id=id)
        idc.delete()

###########################mixins########################
from rest_framework import mixins,generics

class IdcList_v4(generics.GenericAPIView,
                 mixins.ListModelMixin, #ListModelMixin相当于get，展示所有列表
                 mixins.CreateModelMixin): #CreateModelMixin当当于post，创建数据

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self,request,*args,**kwargs):
        """获取所有数据"""
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        """创建数据"""
        return self.create(request,*args,**kwargs)


class IdcDetail_v4(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,#RetrieveModelMixin相当于get,指定某条记录
                   mixins.UpdateModelMixin, #UpdateModelMixin相当于put，修改某条数据
                   mixins.DestroyModelMixin): #DestroyModelMixin相当于delete，删除某条记录

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    lookup_field = "id" #URL关键字参数

    def get(self,request,*args,**kwargs):
        """获取某一条数据"""
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        """更新某一条数据"""
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        """删除数据"""
        return self.destroy(request,*args,**kwargs)



class IdcList_v5(generics.ListCreateAPIView):
    #ListCreateAPIView相当于get与post的混合使用,可以列出所有数据，创建新的数据
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer


class IdcDetail_v5(generics.RetrieveUpdateDestroyAPIView):
    #RetrieveUpdateDestroyAPIView相当于get某一条数据，put某一条数据，delete某一条数据
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    lookup_field = "id" #URL关键字参数




###########视图集

from rest_framework import viewsets

class IdcListViewset(viewsets.ModelViewSet):
    """
    Retrieve:
        返回单个IDC信息
    List:
        返回IDC例表
    update:
        更新IDC信息
    destroy:
        删除IDC记录
    create:
        创建IDC记录
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    lookup_field = "id" #URL关键字参数