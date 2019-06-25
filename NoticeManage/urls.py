# coding:utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_view, name='notice_view'),
    path('list/', views.notice_table_list, name='notice_list'),
    path('action/', views.notice_action, name='notice_action'),
    path('readall/', views.notice_readall, name='notice_read_all'),
    path('count/', views.notice_count, name='notice_count'),
    path('read/<str:notice_id>/', views.notice_read, name='notice_read'),
]
