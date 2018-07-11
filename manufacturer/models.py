from django.db import models


class Manufacturer(models.Model):
    """
    制造商
    """
    vendor_name     = models.CharField("厂商名称",max_length=32,db_index=True,unique=True,help_text="厂商名称")
    tel             = models.CharField("联系电话",null=True,max_length=15,help_text="联系电话")
    mail            = models.EmailField("邮件地址",null=True,help_text="email")
    remark          = models.CharField("备注",null=True,max_length=300,help_text="备注")

    def __str__(self):
        return self.vendor_name

    class Meta:
        db_table = "resources_manufacturer"
        ordering = ["-id"]


class ProductModel(models.Model):
    """
    产品型号
    """
    model_name      = models.CharField("型号名称",max_length=20,help_text="型号名称")
    vendor          = models.ForeignKey(Manufacturer,verbose_name="所属制造商",help_text="所属制造商")

    def __str__(self):
        return self.model_name

    class Meta:
        db_table = "resources_productmodel"
        ordering = ["-id"]


