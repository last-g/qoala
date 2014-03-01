from django import forms

__author__ = 'Last G'


class TokenAuthForm(forms.Form):
    token = forms.CharField()