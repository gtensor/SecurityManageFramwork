# Generated by Django 2.2.1 on 2019-05-25 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SeMFSetting', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AssetManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=50, verbose_name='任务编号')),
                ('scan_id', models.CharField(max_length=100, null=True, verbose_name='扫描编号')),
                ('task_name', models.CharField(max_length=30, verbose_name='任务名称')),
                ('task_type', models.CharField(choices=[('安全扫描', '安全扫描'), ('扫描同步', '扫描同步')], max_length=25, verbose_name='任务类型')),
                ('task_target', models.TextField(null=True, verbose_name='任务目标')),
                ('task_targetinfo', models.TextField(verbose_name='任务描述')),
                ('task_status', models.CharField(choices=[('0', '审批中'), ('1', '待执行'), ('2', '执行中'), ('3', '已暂停'), ('4', '已完成'), ('5', '已结束')], max_length=20, verbose_name='任务状态')),
                ('task_plan_time', models.DateTimeField(blank=True, null=True, verbose_name='计划执行时间')),
                ('task_plan_end_time', models.DateTimeField(null=True, verbose_name='计划结束时间')),
                ('request_status', models.CharField(choices=[('0', '审批中'), ('1', '审批通过'), ('2', '审批拒绝')], max_length=50, verbose_name='请求状态')),
                ('request_note', models.TextField(null=True, verbose_name='审批备注')),
                ('task_starttime', models.DateTimeField(auto_now_add=True, verbose_name='开始时间')),
                ('task_endtime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('action_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='taskrequestaction_for_user', to=settings.AUTH_USER_MODEL)),
                ('scanner_police', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='police_to_scanner', to='SeMFSetting.ScannerPolicies', verbose_name='扫描策略')),
                ('task_asset', models.ManyToManyField(related_name='asset_to_task', to='AssetManage.Asset', verbose_name='资产关联')),
                ('task_scanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanner_to_task', to='SeMFSetting.Scanner', verbose_name='扫描器')),
                ('task_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_for_user', to=settings.AUTH_USER_MODEL, verbose_name='任务用户')),
            ],
        ),
    ]
