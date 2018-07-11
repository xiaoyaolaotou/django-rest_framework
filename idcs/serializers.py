from rest_framework import serializers
from rest_framework import status
from .models import Idc

class IdcSerializer(serializers.Serializer):
    """
    Idc序列化类
    """
    id          = serializers.IntegerField(read_only=True)
    name        = serializers.CharField(required=True,max_length=32,
                                        label="机房名称",
                                        help_text='机房名称',
                                        error_messages={'blank':"这个字段不能为空"})
    address     = serializers.CharField(required=True,max_length=256,
                                        label="机房地址",
                                        help_text="机房地址",
                                        error_messages = {'blank': "这个字段不能为空"})

    phone       = serializers.CharField(required=True,max_length=15,
                                        label="联系电话",
                                        help_text="联系电话",
                                        error_messages = {'blank': "这个字段不能为空"})
    email       = serializers.CharField(required=True,label="email",
                                        help_text="email",
                                        error_messages={'blank': "这个字段不能为空"})
    letter      = serializers.CharField(required=True,label="字母简称",
                                        max_length=5,
                                        help_text="字母简称",
                                        error_messages={'blank': "这个字段不能为空"})

    def create(self, validated_data):
        """创建用户请求过来的数据"""
        return Idc.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """序列化更新用户过来的数据"""
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.phone = validated_data['phone']
        instance.email = validated_data['email']
        instance.letter = validated_data['letter']
        instance.save()
        return instance

