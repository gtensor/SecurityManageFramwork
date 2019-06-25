# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .. import models, forms


@login_required
@csrf_protect
def os_info_update(request, os_id):
    user = request.user
    error = ''
    if user.is_superuser:
        os_info = get_object_or_404(models.OSInfo, id=os_id)
    else:
        os_info = get_object_or_404(models.OSInfo, asset__asset_user=user, id=os_id)
    if request.method == 'POST':
        form = forms.OSInfoForm(request.POST, instance=os_info)
        if form.is_valid():
            form.save()
            error = '信息已更新'
        else:
            error = '请检查输入'
    else:
        form = forms.OSInfoForm(instance=os_info)
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'asset_os_info_update',
                   'argu': os_id, 'error': error})


@login_required
@csrf_protect
def internet_info_update(request, internet_id):
    user = request.user
    error = ''
    if user.is_superuser:
        internet_info = get_object_or_404(models.InternetInfo, id=internet_id)
    else:
        internet_info = get_object_or_404(models.InternetInfo, asset__asset_user=user, id=internet_id)
    if request.method == 'POST':
        form = forms.InternetInfoForm(request.POST, instance=internet_info)
        if form.is_valid():
            form.save()
            error = '信息已更新'
        else:
            error = '请检查输入'
    else:
        form = forms.InternetInfoForm(instance=internet_info)
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'asset_internet_info_update',
                   'argu': internet_id, 'error': error})
