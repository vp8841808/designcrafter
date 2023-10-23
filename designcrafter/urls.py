"""
URL configuration for designcrafter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from designcrafter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('registration',views.registration),
    path('sendotp',views.sendotp),
    path('user_login',views.user_login),
    path('verify_otp',views.verify_otp),
    path('userlogin_page',views.userlogin_page),
    path('userlogin',views.userlogin),
    path('user_session',views.user_session),
    path('dashboard',views.dashboard),
    path('desgignuploadpage',views.desgignuploadpage),
    path('designupload',views.designupload),
]
