from rest_framework import serializers
from idcs.serializers import IdcSerializer
from .models import Cabinet
from idcs.models import Idc

class CabinetSerializer(serializers.Serializer):
    """
    序列化机柜
    """
    idc  = serializers.PrimaryKeyRelatedField(many=False,queryset=Idc.objects.all())#进行多对一进行关联序列化
    #idc  = serializers.CharField(source="idc.name")
    name = serializers.CharField(required=True)

    def to_representation(self, instance):
        """把上面的成员中属性序列化成想要自己实现的json格式"""
        idc_obj = instance.idc
        print(idc_obj)
        ret = super(CabinetSerializer,self).to_representation(instance)#根据上面要显示返回的数据
        ret["idc"] = {
            "id":idc_obj.id,
            "name":idc_obj.name
        }
        return ret


    def to_internal_value(self, data):
        """
        反序列化第一步：拿到的是用户提交过来的原始数据,自己处理可以入库
        :param self:
        :param data:
        :return:
        """
        return super(CabinetSerializer,self).to_internal_value(data)


    def create(self, validated_data):
        """反序列化创建数据"""
        return Cabinet.objects.create(**validated_data)