"""hengDaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
#from itertools import product
import django
from django.contrib import admin
from django.urls import path
from homeapp.views import home  # 导入首页对应的视图处理函数
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),        # 添加“首页”应用
    path('aboutApp/', include('aboutApp.urls')),    # 添加公司简介路由
    path('contactApp/', include('contactApp.urls')),
    path('newsApp/', include('newsApp.urls')),
    path('productsApp/', include('productsApp.urls')),
    path('scienceApp/', include('scienceApp.urls')),
    path('serviceApp/', include('serviceApp.urls')),
    path('ueditor/', include('DjangoUeditor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)