# coding:utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('', views.chartview, name='chart_view'),
    path('assettype/', views.getassettype, name='chart_asset_type'),
    path('vulnleave/', views.getvulnleave, name='chart_vuln_leave'),
    path('vulnstatus/', views.getvulnstatus, name='chart_vuln_status'),
    path('vulnname/', views.getvulnname, name='chart_vuln_name'),
    path('getdatemonth/', views.getdatemonth, name='chart_get_date_month'),
]
