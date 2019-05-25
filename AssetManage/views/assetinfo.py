# coding:utf-8

'''
Created on 2018年5月18日

@author: yuguanc
'''
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .. import models, forms


@login_required
@csrf_protect
def osinfpupdate(request, os_id):
    user = request.user
    error = ''
    if user.is_superuser:
        osinfo = get_object_or_404(models.OSInfo, id=os_id)
    else:
        osinfo = get_object_or_404(models.OSInfo, asset__asset_user=user, id=os_id)
    if request.method == 'POST':
        form = forms.OS_Info_form(request.POST, instance=osinfo)
        if form.is_valid():
            form.save()
            error = '信息已更新'
        else:
            error = '请检查输入'
    else:
        form = forms.OS_Info_form(instance=osinfo)
    return render(request, 'formupdate.html',
                  {'form': form, 'post_url': 'assetosinfoupdate', 'argu': os_id, 'error': error})


@login_required
@csrf_protect
def internetinfpupdate(request, internet_id):
    user = request.user
    error = ''
    if user.is_superuser:
        internetinfo = get_object_or_404(models.InternetInfo, id=internet_id)
    else:
        internetinfo = get_object_or_404(models.InternetInfo, asset__asset_user=user, id=internet_id)
    if request.method == 'POST':
        form = forms.InternetInfoForm(request.POST, instance=internetinfo)
        if form.is_valid():
            form.save()
            error = '信息已更新'
        else:
            error = '请检查输入'
    else:
        form = forms.InternetInfoForm(instance=internetinfo)
    return render(request, 'formupdate.html',
                  {'form': form, 'post_url': 'assetinternetinfoupdate', 'argu': internet_id, 'error': error})
