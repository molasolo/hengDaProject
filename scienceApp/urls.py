from django.urls import path
from . import views

app_name = 'scienceApp' # 设置应用名

urlpatterns = [
    path('scienceApp/', views.science, name='science'),
]