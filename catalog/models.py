from django.db import models

# Create your models here.

from django.urls import reverse  # To generate URLS by reversing URL patterns


import uuid  # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User  # Required to assign User as a borrower

#######################

#批次数据
class  pici_data(models.Model):
    picihao = models.CharField(max_length=200)
    pinpai = models.CharField(max_length=50)
    shengchan_date = models.DateField()
    #开包
    kaibao_up_time = models.DateTimeField()
    kaibao_down_time = models.DateTimeField()
    kaibao_weight = models.CharField(max_length=20)
    #松散
    songsan_up_time = models.DateTimeField()
    songsan_down_time = models.DateTimeField()
    songsan_weight = models.CharField(max_length=20)
    songsan_shuifen_value = models.CharField(max_length=20)
    songsan_wendu_value = models.CharField(max_length=20)
    songsan_rate = models.CharField(max_length=20)
    #加料
    jialiao_up_time = models.DateTimeField(default="")
    jialiao_down_time = models.DateTimeField(default="")
    jialiao_weight = models.CharField(max_length=20,default="")
    jialiao_jingdu = models.CharField(max_length=20,default="")
    jialiao_wendu_value = models.CharField(max_length=20,default="")
    jialiao_shuifen_value = models.CharField(max_length=20,default="")
    #储叶
    chugui_bianhao = models.CharField(max_length=20,default="")
    jingui_kaishi_time = models.DateTimeField(default="")
    jingui_jieshu_time = models.DateTimeField(default="")
    chugui_kaishi_time = models.DateTimeField(default="")
    chugui_jieshu_time = models.DateTimeField(default="")
    #切丝

    def get_pici_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('pici-detail', args=[str(self.id)])

    def __str__(self):
        return self.picihao
