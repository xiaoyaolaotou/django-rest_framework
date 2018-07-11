from django.db import models
from idcs.models import Idc


class Cabinet(models.Model):
    """机柜"""
    idc     = models.ForeignKey(Idc,verbose_name="所在机房")
    name    = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "resources_cabinet"
        ordering = ['id']