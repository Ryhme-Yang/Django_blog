# -*- coding: UTF-8 -*-
from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta: #TopicForm类中的嵌套类Meta
        model=Topic
        fields=['text']
        labels={'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}  #默认小部件widgets的大小设置宽度为80列，而不是默认的40列