from django.shortcuts import render,redirect,HttpResponse
from .models import pici_data,chenben_test_data,furongwang_gongshi_test_data,baisha_gongshi_test_data
# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,JsonResponse

from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.template import Template
# from .forms import RenewBookForm

import json
@login_required()
def index(request):
    #model = chenben_test_data
    try:
        chenben_test_data_model = chenben_test_data.objects.get(id=1)
        data_1 = [chenben_test_data_model.chusilv_data,
                chenben_test_data_model.huishouyansi_data,
                chenben_test_data_model.danxianghaoye_data,
                chenben_test_data_model.guochengxiaohao_data,
                chenben_test_data_model.renyuanxiaohao_data,
                chenben_test_data_model.nenghao_data]
    except chenben_test_data.DoesNotExist:
        data_1 = [0,0,0,0,0,0]
    
    print(data_1)
    
    try:
        furongwang_gongshi_test_data_model = furongwang_gongshi_test_data.objects.get(id=1)
        data_6 = [furongwang_gongshi_test_data_model.riqi_1,
                  furongwang_gongshi_test_data_model.riqi_2,
                  furongwang_gongshi_test_data_model.riqi_3,
                  furongwang_gongshi_test_data_model.riqi_4,
                  furongwang_gongshi_test_data_model.riqi_5,
                  furongwang_gongshi_test_data_model.riqi_6,
                  furongwang_gongshi_test_data_model.riqi_7,
                  furongwang_gongshi_test_data_model.riqi_8,
                  furongwang_gongshi_test_data_model.riqi_9,
                  furongwang_gongshi_test_data_model.riqi_10,
                  furongwang_gongshi_test_data_model.riqi_11,
                  furongwang_gongshi_test_data_model.riqi_12,
                  furongwang_gongshi_test_data_model.riqi_13,
                  furongwang_gongshi_test_data_model.riqi_14,
                  furongwang_gongshi_test_data_model.riqi_15,
                  furongwang_gongshi_test_data_model.riqi_16,
                  furongwang_gongshi_test_data_model.riqi_17,
                  furongwang_gongshi_test_data_model.riqi_18,
                  furongwang_gongshi_test_data_model.riqi_19,
                  furongwang_gongshi_test_data_model.riqi_20,
                  furongwang_gongshi_test_data_model.riqi_21,
                  furongwang_gongshi_test_data_model.riqi_22,
                  furongwang_gongshi_test_data_model.riqi_23,
                  furongwang_gongshi_test_data_model.riqi_24,
                  furongwang_gongshi_test_data_model.riqi_25,
                  furongwang_gongshi_test_data_model.riqi_26,
                  furongwang_gongshi_test_data_model.riqi_27,
                  furongwang_gongshi_test_data_model.riqi_28,
                  furongwang_gongshi_test_data_model.riqi_29,
                  furongwang_gongshi_test_data_model.riqi_30,
                  furongwang_gongshi_test_data_model.riqi_31]
    except furongwang_gongshi_test_data.DoesNotExist:
        data_6 =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    try:
        baisha_gongshi_test_data_model = baisha_gongshi_test_data.objects.get(id=1)
        data_7 = [baisha_gongshi_test_data_model.riqi_1,
                  baisha_gongshi_test_data_model.riqi_2,
                  baisha_gongshi_test_data_model.riqi_3,
                  baisha_gongshi_test_data_model.riqi_4,
                  baisha_gongshi_test_data_model.riqi_5,
                  baisha_gongshi_test_data_model.riqi_6,
                  baisha_gongshi_test_data_model.riqi_7,
                  baisha_gongshi_test_data_model.riqi_8,
                  baisha_gongshi_test_data_model.riqi_9,
                  baisha_gongshi_test_data_model.riqi_10,
                  baisha_gongshi_test_data_model.riqi_11,
                  baisha_gongshi_test_data_model.riqi_12,
                  baisha_gongshi_test_data_model.riqi_13,
                  baisha_gongshi_test_data_model.riqi_14,
                  baisha_gongshi_test_data_model.riqi_15,
                  baisha_gongshi_test_data_model.riqi_16,
                  baisha_gongshi_test_data_model.riqi_17,
                  baisha_gongshi_test_data_model.riqi_18,
                  baisha_gongshi_test_data_model.riqi_19,
                  baisha_gongshi_test_data_model.riqi_20,
                  baisha_gongshi_test_data_model.riqi_21,
                  baisha_gongshi_test_data_model.riqi_22,
                  baisha_gongshi_test_data_model.riqi_23,
                  baisha_gongshi_test_data_model.riqi_24,
                  baisha_gongshi_test_data_model.riqi_25,
                  baisha_gongshi_test_data_model.riqi_26,
                  baisha_gongshi_test_data_model.riqi_27,
                  baisha_gongshi_test_data_model.riqi_28,
                  baisha_gongshi_test_data_model.riqi_29,
                  baisha_gongshi_test_data_model.riqi_30,
                  baisha_gongshi_test_data_model.riqi_31]
    except baisha_gongshi_test_data.DoesNotExist:
        data_7 =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(data_6)
    print(data_7)
    #data_1 = [9,19,29,39,49,59]
    data_2 = [100, 8, 1200, 50, 0]
    data_3 = [100, 100, 100, 100, 100]
    data_4 =  [ [24, 40, 101, 134, 90, 230, 210, 230, 120, 230, 210, 120],
                [40, 64, 191, 324, 290, 330, 310, 213, 180, 200, 180, 79]
              ]
    data_5 =  [ [123, 175, 112, 197, 121, 67, 98, 21, 43, 64, 76, 38],
                [143, 131, 165, 123, 178, 21, 82, 64, 43, 60, 19, 34]
              ]
    #data_6 =  [30, 40, 30, 40, 30, 40, 30, 60, 20, 40, 30, 40, 30, 40, 30, 40, 30, 60, 20, 40, 30, 40, 30, 40, 30, 40, 20, 60, 50, 40]
    #data_7 =  [130, 10, 20, 40, 30, 40, 80, 60, 20, 40, 90, 40, 20, 140, 30, 40, 130, 20, 20, 40, 80, 70, 30, 40, 30, 120, 20, 99, 50, 20]
    data_8 = 30348
    data_9 = 34235
    return render(request, 'index.html',{'data_1':data_1,'data_2':data_2,'data_3':data_3,'data_4':data_4,'data_5':data_5,'data_6':data_6,'data_7':data_7,'data_8':data_8,'data_9':data_9})

def more_cps(request):
    return render(request,'home.html')

def zhisi_echarts(request):
    return render(request,'index.html')

def re_home(request):
    return render(request,'index.html')

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_auth(request):
     """
     :return:
     成功：重定向到首页
     失败：返回login页面，并提示错误
     """
     #return render(request, "index.html")
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(username=username, password=password)
     if user is not None:
        login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session
        #return render(request, "index.html")
        return redirect("/catalog/index/")
     else:
        return render(request, 'login.html', {'error': '用户名户密码错误！'})
        return redirect("/login/")

def my_login(request):
     """
     :param request
     :return: 展示登录页面
     """
     return render(request, "login.html")
    
    
@login_required()
def my_logout(request):
     """
     :param request
     :return: 退出并重定向到登录页面
     """
     logout(request)
     return redirect("/login/")
    
    
#@login_required()
#def index(request):
#     """
#    :param request
#   :return: 用户首页
#   """
#  return render(request, "index.html")



from django.views import generic

class pici_data_list_view(generic.ListView):
    model = pici_data
    paginate_by = 10

    #时间倒序，过滤数据
    def get_queryset(self):
        return pici_data.objects.order_by('shengchan_date')

class pici_data_list_baisha_view(generic.ListView):
    model = pici_data
    paginate_by = 10

    #时间倒序，过滤数据
    def get_queryset(self):
        return pici_data.objects.filter(pinpai = '白沙').order_by('shengchan_date')

class pici_data_list_gengxian_view(generic.ListView):
    model = pici_data
    paginate_by = 10

    #时间倒序，过滤数据
    def get_queryset(self):
        return pici_data.objects.filter(pinpai = '梗线').order_by('shengchan_date')

#class pici_detail_view(generic.DateDetailView):
#    model = pici_data

def pici_detail_view(request,pk):
    pici_id=pici_data.objects.get(pk=pk)
    #book_id=get_object_or_404(Book, pk=pk)
    return render(
        request,
        'catalog/pici_detail.html',
        context={'pici_data':pici_id,}
    )
