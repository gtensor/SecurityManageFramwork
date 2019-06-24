# -*- coding: utf-8 -*-

from django.forms import ModelForm
from . import models
from django.forms import widgets


class ArticleEditForm(ModelForm):
    class Meta:
        model = models.Article
        fields = ['article_name', 'article_type', 'article_body', 'file']
        widgets = {
            'article_name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': '文章名称'}),
            'article_type': widgets.Select(attrs={'class': 'form-control'}),
            'article_body': widgets.Textarea(attrs={'class': 'form-control', 'placeholder': '知识库内容'}),
            'file': widgets.FileInput(),
        }


class ArticleCommentEditForm(ModelForm):
    class Meta:
        model = models.ArticleComments
        fields = ['article_comment_body']
        widgets = {
            'article_comment_body': widgets.TextInput(attrs={'class': 'form-control'}),
        }
