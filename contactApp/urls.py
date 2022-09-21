from django.urls import path
from . import views

app_name = 'contactApp' # 设置应用名

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('recruit/', views.recruit, name='recruit'),
]