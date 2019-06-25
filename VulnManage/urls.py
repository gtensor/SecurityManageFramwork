# coding:utf-8
'''
Created on 2018年5月14日

@author: yuguanc
'''
from django.urls import path
from .views import views, cnvdviews

urlpatterns = [
    path('user/', views.vulnview, name='vuln_view'),
    path('user/list/', views.vulntablelist, name='vuln_list'),
    path('user/listfix/', views.vulnfixlist, name='vuln_list_fix'),
    path('user/fix/<str:vuln_id>/', views.vuln_change_status, name='vuln_fix'),
    path('user/details/<str:vuln_id>/', views.vulndetails, name='vuln_details'),

    path('cnvd/', cnvdviews.cnvdvuln_view, name='cnvd_vuln_view'),
    path('cnvd/list/', cnvdviews.cnvdvulntablelist, name='cnvd_vuln_list'),
    path('cnvd/update/<str:cnvdvuln_id>', cnvdviews.cnvdvuln_update, name='cnvd_vuln_update'),
    path('cnvd/details/<str:cnvdvuln_id>', cnvdviews.cnvdvulndetails, name='cnvd_vuln_details'),
    path('cnvd/vulnrenew/', cnvdviews.renew, name='cnvd_vuln_renew'),

    path('manage/create/<str:asset_id>/', views.vulncreate, name='vuln_create'),
    path('manage/update/<str:vuln_id>/', views.vuln_update, name='vuln_update'),
]
