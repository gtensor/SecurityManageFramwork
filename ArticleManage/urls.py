#! /usr/bin/python3
# -*- coding:UTF-8 -*-

from django.urls import path

from . import views


urlpatterns = [
    path('user/', views.vuln_view, name='article_view'),
    path('user/list/', views.articleable_list, name='article_list'),
    path('user/details/<str:article_id>/', views.article_details, name='article_details'),
    
    path('manage/create/', views.article_create, name='article_create'),
    path('manage/update/<str:article_id>/', views.article_update, name='article_update'),
    path('manage/delete/<str:article_id>/', views.article_delete, name='article_delete'),
    path('manage/revoke/<str:article_id>/', views.article_revoke, name='article_revoke'),
    path('manage/public/<str:article_id>/', views.article_public, name='article_public'),
    
    path('manage/imgupload/', views.upload_image, name='img_upload'),
]
