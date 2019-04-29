from django import forms
from django.core.exceptions import ValidationError
import hashlib

from web import models


class BSForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field, forms.BooleanField):
                field.widget.attrs.update({'class': 'form-control'})


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='用户名:',
        strip=True,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        error_messages={
            "required": "不能为空",
        },
    )
    password = forms.CharField(
        label='密码:',
        required=True,
        strip=True,
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}),
        error_messages={
            "required": "不能为空",
        }
    )


class RegForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        exclude = ['is_active']

        labels = {
            'username': '用户名',
        }
        required = {
            'fields': True,
        }
        error_messages = {
            'username': {"required": "不能为空", }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})



class BolgForm(BSForm):
    class Meta:
        model = models.Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
