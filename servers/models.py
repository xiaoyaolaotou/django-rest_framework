from django.db import models
from manufacturer.models import Manufacturer,ProductModel
from idcs.models import Idc
from cabinet.models import Cabinet

class Server(models.Model):
    """
    服务器采集信息
    """
    ip          = models.CharField("业务IP",max_length=15,db_index=True,unique=True,help_text="业务IP")
    hostname    = models.CharField("主机名",max_length=20,db_index=True,unique=True,help_text="主机名")
    cpu         = models.CharField("CPU",max_length=100,help_text="CPU")
    mem         = models.CharField("mem",max_length=32,help_text="内存")
    disk        = models.CharField("磁盘",max_length=300,help_text="磁盘")
    os          = models.CharField("OS",max_length=50,help_text="操作系统")
    sn          = models.CharField("SN",max_length=100,db_index=True,help_text="SN号")
    manufacturer= models.ForeignKey(Manufacturer,verbose_name="所属制造商",help_text="所属制造商")
    model_name  = models.ForeignKey(ProductModel,verbose_name="所属产品型号",help_text="所属产品型号")
    rmt_card_ip = models.CharField("远程管理卡IP",max_length=15,db_index=True,unique=True,help_text="远程管理卡IP")
    idc         = models.ForeignKey(Idc,verbose_name="所在机房",null=True,help_text="所在机房")
    cabinet     = models.ForeignKey(Cabinet,verbose_name="所在机柜",help_text="所在机柜",null=True)
    cabinet_position = models.CharField("机柜内位置",max_length=20,null=True,help_text="机柜内位置")
    uuid        = models.CharField("UUID",max_length=100,db_index=True,unique=True,help_text="UUID")
    last_check  = models.DateTimeField("最后检查时间",auto_now=True,help_text="最后检查时间")
    remark = models.CharField("备注", max_length=300, null=True, help_text="备注")

    def __str__(self):
        return self.ip

    class Meta:
        db_table = "resources_server"
        ordering = ['id']


class NetworkDevice(models.Model):
    """
    网卡模型
    """
    name        = models.CharField("网卡设备名",max_length=20,help_text="网卡设备名")
    mac         = models.CharField("MAC地址",max_length=17,help_text="MAC地址")
    host        = models.ForeignKey(Server,verbose_name="所在服务器",help_text="所在服务器")
    remark      = models.CharField("备注",max_length=300,null=True,help_text="备注")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "resources_network_device"
        ordering = ['-id']


class IP(models.Model):
    """
    IP模型
    """
    ip_addr        = models.CharField("ip地址",max_length=15,db_index=True,unique=True,help_text="ip地址")
    netmask        = models.CharField("子网掩码",max_length=15,help_text="子网掩码")
    device         = models.ForeignKey(NetworkDevice,verbose_name="所在网卡",help_text="verbose_name")
    remark         = models.CharField("备注",max_length=200,null=True,help_text="备注")

    def __str__(self):
        return self.ip_addr

    class Meta:
        db_table = "resources_ip"
        ordering = ["-id"]




