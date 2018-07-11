from rest_framework import serializers
from .models import Manufacturer,ProductModel

class ManufacturerSerializers(serializers.ModelSerializer):
    """
    制造商序列化
    """

    class Meta:
        model = Manufacturer
        fields = "__all__"

    def create(self, validated_data):
        return Manufacturer.objects.create(**validated_data)


class ProductModelSerializers(serializers.ModelSerializer):
    """
    产品型号序列化
    """

    class Meta:
        model = ProductModel
        fields = "__all__"
        # depth = 1

    # def validate(self, attrs):
    #     return attrs
    def validate_model_name(self, attrs):
        """
        验证产品型号不能重复
        :param attrs:
        :return:
        """
        if ProductModel.objects.get(model_name=attrs):
            raise serializers.ValidationError('该产品已存在')
        return attrs


    def to_representation(self, instance):
        """
        自定义显示想要的数据
        :param instance:
        :return:
        """
        vendor = instance.vendor
        ret = super(ProductModelSerializers,self).to_representation(instance)
        ret["vendor"] = {
            "id":vendor.id,
            "name":vendor.vendor_name
        }
        return ret

    def create(self, validated_data):
        return ProductModel.objects.create(**validated_data)






