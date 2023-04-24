from django.shortcuts import render
from .models import pici_data
# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required, permission_required

# from .forms import RenewBookForm


@login_required()
def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects

     #Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'index.html'
    )

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