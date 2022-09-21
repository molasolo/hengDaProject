from django.urls import path
from . import views

app_name = 'newsApp'    # 设置应用名

urlpatterns = [
    path('company/', views.company, name='company'),
    path('industry/', views.industry, name='industry'),
    path('notice/', views.notice, name='notice'),
]
