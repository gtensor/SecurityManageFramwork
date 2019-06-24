# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .. import models, forms


@login_required
@csrf_protect
def port_create(request, asset_id):
    user = request.user
    error = ''
    if user.is_superuser:
        asset = get_object_or_404(models.Asset, asset_id=asset_id)
    else:
        asset = get_object_or_404(models.Asset, asset_user=user, asset_id=asset_id)
    if request.method == 'POST':
        form = forms.AssetPortInfo(request.POST)
        if form.is_valid():
            port = form.cleaned_data['port']
            name = form.cleaned_data['name']
            product = form.cleaned_data['product']
            version = form.cleaned_data['version']
            port_info = form.cleaned_data['port_info']
            models.PortInfo.objects.get_or_create(
                port=port,
                name=name,
                product=product,
                version=version,
                port_info=port_info,
                asset=asset
            )
            error = '添加成功'
        else:
            error = '请检查输入'
    else:
        form = forms.AssetPortInfo()
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'port_create', 'argu': asset_id, 'error': error})


@login_required
@csrf_protect
def port_update(request, port_id):
    user = request.user
    error = ''
    if user.is_superuser:
        port = get_object_or_404(models.PortInfo, id=port_id)
    else:
        port = get_object_or_404(models.PortInfo, asset__asset_user=user, id=port_id)
    if request.method == 'POST':
        form = forms.AssetPortInfo(request.POST, instance=port)
        if form.is_valid():
            form.save()
            error = '端口信息已更新'
        else:
            error = '请检查输入'
    else:
        form = forms.AssetPortInfo(instance=port)
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'port_update', 'argu': port_id, 'error': error})


@login_required
def port_delete(request, port_id):
    user = request.user
    error = ''
    if user.is_superuser:
        port = get_object_or_404(models.PortInfo, id=port_id)
    else:
        port = get_object_or_404(models.PortInfo, asset__asset_user=user, id=port_id)
    if port:
        port.delete()
        error = '删除成功'
    else:
        error = '非法参数'
    return JsonResponse({'error': error})
