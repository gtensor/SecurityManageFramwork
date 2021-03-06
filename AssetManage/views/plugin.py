# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .. import models, forms


@login_required
@csrf_protect
def plugin_create(request, asset_id):
    user = request.user
    error = ''
    if user.is_superuser:
        asset = get_object_or_404(models.Asset, asset_id=asset_id)
    else:
        asset = get_object_or_404(models.Asset, asset_user=user, asset_id=asset_id)
    if request.method == 'POST':
        form = forms.AssetPluginInfo(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            version = form.cleaned_data['version']
            plugin_info = form.cleaned_data['plugin_info']
            models.PluginInfo.objects.get_or_create(
                name=name,
                version=version,
                plugin_info=plugin_info,
                asset=asset
            )
            error = '添加成功'
        else:
            error = '请检查输入'
    else:
        form = forms.AssetPluginInfo()
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'plugin_create', 'argu': asset_id, 'error': error})


@login_required
@csrf_protect
def plugin_update(request, plugin_id):
    user = request.user
    error = ''
    if user.is_superuser:
        plugin = get_object_or_404(models.PluginInfo, id=plugin_id)
    else:
        plugin = get_object_or_404(models.PluginInfo, asset__asset_user=user, id=plugin_id)
    if request.method == 'POST':
        form = forms.AssetPluginInfo(request.POST, instance=plugin)
        if form.is_valid():
            form.save()
            error = '添加成功'
        else:
            error = '请检查输入'
    else:
        form = forms.AssetPluginInfo(instance=plugin)
    return render(request, 'form_update.html',
                  {'form': form, 'post_url': 'plugin_update', 'argu': plugin_id, 'error': error})


@login_required
def plugin_delete(request, plugin_id):
    user = request.user
    error = ''
    if user.is_superuser:
        plugin = get_object_or_404(models.PluginInfo, id=plugin_id)
    else:
        plugin = get_object_or_404(models.PluginInfo, asset__asset_user=user, id=plugin_id)
    if plugin:
        plugin.delete()
        error = '删除成功'
    else:
        error = '非法参数'
    return JsonResponse({'error': error})
