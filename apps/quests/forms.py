# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django import forms
from .models import QuestAnswer
from django.utils.translation import ugettext as _

__author__ = 'Last G'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = QuestAnswer
        fields = ['answer']
        widgets = {
            'answer': forms.TextInput(),
        }
        labels = {
            'answer': _('Flag'),
        }
        help_texts = {
            'answer': _('Please provide flag here'),
        }
