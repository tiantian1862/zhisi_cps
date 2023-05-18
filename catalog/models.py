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
    
class chenben_test_data(models.Model):
    #成本数据字段
    chusilv_data = models.CharField(max_length=20)
    huishouyansi_data = models.CharField(max_length=20)
    danxianghaoye_data = models.CharField(max_length=20)
    guochengxiaohao_data = models.CharField(max_length=20)
    renyuanxiaohao_data = models.CharField(max_length=20)
    nenghao_data = models.CharField(max_length=20)
    time = models.DateTimeField()

class furongwang_gongshi_test_data(models.Model):
    yuefen_time = models.DateTimeField()
    riqi_1 = models.CharField(max_length=10)
    riqi_2 = models.CharField(max_length=10)
    riqi_3 = models.CharField(max_length=10)
    riqi_4 = models.CharField(max_length=10)
    riqi_5 = models.CharField(max_length=10)
    riqi_6 = models.CharField(max_length=10)
    riqi_7 = models.CharField(max_length=10)
    riqi_8 = models.CharField(max_length=10)
    riqi_9 = models.CharField(max_length=10)
    riqi_10 = models.CharField(max_length=10)
    riqi_11 = models.CharField(max_length=10)
    riqi_12 = models.CharField(max_length=10)
    riqi_13 = models.CharField(max_length=10)
    riqi_14= models.CharField(max_length=10)
    riqi_15= models.CharField(max_length=10)
    riqi_16= models.CharField(max_length=10)
    riqi_17 = models.CharField(max_length=10)
    riqi_18 = models.CharField(max_length=10)
    riqi_19 = models.CharField(max_length=10)
    riqi_20 = models.CharField(max_length=10)
    riqi_21= models.CharField(max_length=10)
    riqi_22 = models.CharField(max_length=10)
    riqi_23 = models.CharField(max_length=10)
    riqi_24 = models.CharField(max_length=10)
    riqi_25= models.CharField(max_length=10)
    riqi_26= models.CharField(max_length=10)
    riqi_27= models.CharField(max_length=10)
    riqi_28= models.CharField(max_length=10)
    riqi_29= models.CharField(max_length=10)
    riqi_30= models.CharField(max_length=10)
    riqi_31= models.CharField(max_length=10)
  

class baisha_gongshi_test_data(models.Model):
    yuefen_time = models.DateTimeField()
    riqi_1 = models.CharField(max_length=10)
    riqi_2 = models.CharField(max_length=10)
    riqi_3 = models.CharField(max_length=10)
    riqi_4 = models.CharField(max_length=10)
    riqi_5 = models.CharField(max_length=10)
    riqi_6 = models.CharField(max_length=10)
    riqi_7 = models.CharField(max_length=10)
    riqi_8 = models.CharField(max_length=10)
    riqi_9 = models.CharField(max_length=10)
    riqi_10 = models.CharField(max_length=10)
    riqi_11 = models.CharField(max_length=10)
    riqi_12 = models.CharField(max_length=10)
    riqi_13 = models.CharField(max_length=10)
    riqi_14= models.CharField(max_length=10)
    riqi_15= models.CharField(max_length=10)
    riqi_16= models.CharField(max_length=10)
    riqi_17 = models.CharField(max_length=10)
    riqi_18 = models.CharField(max_length=10)
    riqi_19 = models.CharField(max_length=10)
    riqi_20 = models.CharField(max_length=10)
    riqi_21= models.CharField(max_length=10)
    riqi_22 = models.CharField(max_length=10)
    riqi_23 = models.CharField(max_length=10)
    riqi_24 = models.CharField(max_length=10)
    riqi_25= models.CharField(max_length=10)
    riqi_26= models.CharField(max_length=10)
    riqi_27= models.CharField(max_length=10)
    riqi_28= models.CharField(max_length=10)
    riqi_29= models.CharField(max_length=10)
    riqi_30= models.CharField(max_length=10)
    riqi_31= models.CharField(max_length=10)


    