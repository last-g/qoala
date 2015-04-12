# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django import forms

__author__ = 'Last G'


class TokenAuthForm(forms.Form):
    token = forms.CharField()