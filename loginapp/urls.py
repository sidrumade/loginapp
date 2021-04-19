from loginapp import views
from django.urls import path,include,re_path

app_name = 'loginapp'

urlpatterns = [
  
    re_path(r'^user_login/$',views.user_login,name='user_login') ,
    re_path(r'^register/$',views.register,name='register') ,
]