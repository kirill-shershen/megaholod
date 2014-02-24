# -*- coding:utf-8 -*-
from django import forms
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder' : 'Имя:'})
        self.fields['email'].widget.attrs.update({'placeholder' : 'Электронная почта:'})
        self.fields['phone'].widget.attrs.update({'placeholder' : 'Телефон:'})
        self.fields['message'].widget.attrs.update({'placeholder' : 'Сообщение:'})
