# coding:utf-8


from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapped_view, name='mapped_view'),
    path('list/', views.mapped_table_list, name='mapped_list'),
    path('create/', views.mapped_create, name='mapped_create'),
    path('update/<str:mapped_id>/', views.mapped_update, name='mapped_update'),
    path('details/<str:mapped_id>/', views.mapped_details, name='mapped_details'),
]
