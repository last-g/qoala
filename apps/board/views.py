# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.serializers.json import DjangoJSONEncoder
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import sys

from .boards import *

def check_is_superuser(user):
    return user.is_superuser

# Create your views here.

def task_board(request):
    tasks_by_category = get_task_board(request.user)
    return render(request, 'board/taskboard.html', {'by_categories': tasks_by_category})


#@condition(last_modified_func=scoreboard_modified)
@user_passes_test(check_is_superuser)
@login_required
def score_board(request):
    scores = get_scoreboard()
    return render(request, 'board/scoreboard.html', {'teams': scores})



def default_request():
    return QuestAnswer.objects.order_by('-created_at', '-id').values(
        'answer', 'result', 'is_checked', 'is_success',
        'quest_variant__quest__shortname', 'quest_variant__team__name',
        'created_at', 'id',
        'quest_variant__quest__score', 'quest_variant__quest__category__name'
    )

@csrf_exempt
@user_passes_test(check_is_superuser)
@login_required
def get_last_answers(request):
    from django.core import serializers

    json_serializer = serializers.get_serializer("json")()

    answ_id = request.POST.get('id', None)
    min_date = request.POST.get('min_date', None)
    task_name = request.POST.get('task_name') or None
    answers = default_request()
    if min_date:
        answers = answers.filter(created_at__gt=min_date)
    if answ_id:
        answers = answers.filter(pk__gt=answ_id)
    if task_name:
        answers = answers.filter(quest_variant__quest_name__contains=task_name)
    if not min_date:
        answers = answers[:50]
#    response = json_serializer.serialize(answers, ensure_ascii=False, indent=2, use_natural_keys=True)
    response = json.dumps(list(answers), cls=DjangoJSONEncoder)
#    response = json_serializer.serialize(list(answers))
    return HttpResponse(response, mimetype="application/json")

@csrf_exempt
@user_passes_test(check_is_superuser)
@login_required
def get_more_answers(request):
    last_id = request.POST['id']
    count = int(request.POST.get('count', 70))
#    max_date = request.POST.get('max_date', None)
#    task_name = request.POST.get('task_name') or None

    answers = default_request().filter(id__lt=last_id)[0:count]
    response = json.dumps(list(answers), cls=DjangoJSONEncoder)
    return HttpResponse(response, mimetype="application/json")


@user_passes_test(check_is_superuser)
@login_required
def answer_board(request):
    answers = default_request()[:50]
    answers_json = json.dumps(list(answers), cls=DjangoJSONEncoder)
    return render(request, 'board/answerboard.html', {'answers' : answers_json})