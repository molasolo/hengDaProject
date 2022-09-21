from django.urls import path
from . import views

app_name = 'scienceApp' # 设置应用名

urlpatterns = [
    path('science/', views.science, name='science'),
]