# -*- coding: utf-8 -*-

from django import forms

from .models import Posting #モデルインポート

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ( 'name', 'post',)