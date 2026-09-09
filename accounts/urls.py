"""为accounts定义URL"""
from django.urls import path,include
from . import views
app_name = "accounts"
urlpatterns = [
    #默认身份验证URL
    path("",include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
]