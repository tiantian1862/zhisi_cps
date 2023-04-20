from django.urls import path,re_path
from . import views




urlpatterns = [
    #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   # url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.my_login, name='my_login'),
    path('login_auth/',views.login_auth,name='login_auth'),
    path('index/', views.index, name='index'),
    path('more_cps/',views.more_cps,name='more_cps'),
    path('pici_data_list/',views.pici_data_list_view.as_view(),name='pici_data_list'),
    #re_path(r'^pici_data/(?P<pk>\d+)/', views.pici_detail_view, name='pici-detail'),
    path('pici_data/<int:pk>', views.pici_detail_view, name='pici-detail'),
    #path('', views.my_login, name='my_login'),
    #path('',views.zhisi_echarts,name='zhisi_echarts')
]