# coding:utf-8
'''
Created on 2018年5月15日

@author: yuguanc
'''

from django.urls import path
from .views import views, assetdetails, port, plugin, file, assetconnect, assetinfo, taskview, handover, csv

urlpatterns = [
    path('user/', views.asset_view, name='asset_view'),
    path('user/list/', views.asset_table_list, name='asset_list'),
    path('user/create/', views.asset_create, name='asset_create'),
    path('user/request/', views.asset_request, name='asset_request'),
    path('user/delete/', views.asset_delete, name='asset_delete'),
    path('user/update/<str:asset_id>/', views.asset_update, name='asset_update'),
    path('user/details/<str:asset_id>/', assetdetails.asset_details_view, name='asset_details'),

    path('user/csv/os/', csv.create_csv_os, name='create_os_csv'),
    path('user/csv/web/', csv.create_csv_web, name='create_web_csv'),
    path('user/csv/vuln/', csv.create_csv_vuln, name='create_vuln_csv'),
    path('user/csv/upload/', csv.file_update, name='create_upload_csv'),

    path('user/handover/', handover.asset_handover, name='asset_hand_over'),

    path('handover/', handover.handoverview, name='asset_handover_view'),
    path('handover/list/', handover.asset_handover_list, name='asset_handover_list'),
    path('handover/action/', handover.asset_handover_action, name='asset_handover_action'),

    path('user/task/', taskview.task_action, name='asset_task_action'),

    path('user/update/osinfo/<str:os_id>/', assetinfo.os_info_update, name='asset_os_info_update'),
    path('user/update/internetinfo/<str:internet_id>/', assetinfo.internet_info_update,
         name='asset_internet_info_update'),

    path('user/port/<str:asset_id>/', assetdetails.asset_ports, name='port_table'),
    path('user/create/port/<str:asset_id>/', port.port_create, name='port_create'),
    path('user/update/port/<str:port_id>/', port.port_update, name='port_update'),
    path('user/delete/port/<str:port_id>/', port.port_delete, name='port_delete'),

    path('user/vuln/<str:asset_id>/', assetdetails.asset_vuln, name='vuln_table'),

    path('user/plugin/<str:asset_id>/', assetdetails.asset_plugin, name='plugin_table'),
    path('user/create/plugin/<str:asset_id>/', plugin.plugin_create, name='plugin_create'),
    path('user/update/plugin/<str:plugin_id>/', plugin.plugin_update, name='plugin_update'),
    path('user/delete/plugin/<str:plugin_id>/', plugin.plugin_delete, name='plugin_delete'),

    path('user/file/<str:asset_id>/', assetdetails.asset_file, name='file_table'),
    path('user/create/file/<str:asset_id>/', file.file_create, name='file_create'),
    path('user/update/file/<str:file_id>/', file.fileupdate, name='file_update'),
    path('user/delete/file/<str:file_id>/', file.filedelete, name='file_delete'),

    path('user/assetconnect/<str:asset_id>/', assetdetails.asset_asset, name='asset_connect_table'),
    path('user/create/assetconnect/<str:asset_id>/', assetconnect.asset_connect_create, name='asset_connect_create'),
    path('user/delete/assetconnect/<str:asset_id>/<str:assetconnect_id>/', assetconnect.asset_connect_delete,
         name='asset_connect_delete'),

    path('request/', views.asset_request_view, name='asset_manage_request'),
    path('request/list/', views.asset_request_list, name='asset_request_list'),
    path('request/action/', views.asset_request_action, name='asset_request_action'),
    path('request/listaction/', views.asset_request_list_action, name='asset_request_list_action'),

    path('manage/', taskview.asset_user_action, name='asset_user_action'),
    path('manage/<str:assetuser_id>/', taskview.asset_user, name='asset_user_do'),

]
