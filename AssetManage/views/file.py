# -*- coding: utf-8 -*-

import uuid

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .. import models, forms


@login_required
@csrf_protect
def file_create(request, asset_id):
    user = request.user
    error = ''
    if user.is_superuser:
        asset = get_object_or_404(models.Asset, asset_id=asset_id)
    else:
        asset = get_object_or_404(models.Asset, asset_user=user, asset_id=asset_id)
    if request.method == 'POST':
        form = forms.FileInfo(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            file_info = form.cleaned_data['file_info']
            file_suffix = file.name.split(".")[-1]
            file_name = str(uuid.uuid1()) + "." + file_suffix
            file.name = file_name
            models.File.objects.get_or_create(
                name=name,
                file=file,
                file_info=file_info,
                asset=asset,
            )
            error = '添加成功'
        else:
            error = '请检查输入'
    else:
        form = forms.FileInfo()
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'file_create', 'argu': asset_id, 'error': error})


@login_required
@csrf_protect
def fileupdate(request, file_id):
    user = request.user
    error = ''
    if user.is_superuser:
        file = get_object_or_404(models.File, id=file_id)
    else:
        file = get_object_or_404(models.File, asset__asset_user=user, id=file_id)
    if request.method == 'POST':
        form = forms.FileInfo(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            error = '此案次已更新'
        else:
            error = '请检查输入'
    else:
        form = forms.FileInfo(instance=file)
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'fileupdate', 'argu': file_id, 'error': error})


@login_required
def filedelete(request, file_id):
    user = request.user
    error = ''
    if user.is_superuser:
        file = get_object_or_404(models.File, id=file_id)
    else:
        file = get_object_or_404(models.File, asset__asset_user=user, id=file_id)
    if file:
        file.delete()
        error = '删除成功'
    else:
        error = '非法参数'
    return JsonResponse({'error': error})
