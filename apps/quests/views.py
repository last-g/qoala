import django
from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template import response
from django.utils.translation import ugettext as _
from . import models
from . import forms
import django.conf

# Create your views here.

def open_task(req, task):
    if not task.is_open_for(req.user):
        return HttpResponseForbidden(_("This task is closed for you"))

    variant = task.get_variant(req.user)
    return render(req, 'quests/open.html', {'variant': variant, 'form': forms.AnswerForm()})


def open_task_by_id(req, task_id):
    task = get_object_or_404(models.Quest, pk=task_id)
    open_task(req, task)


def open_task_by_name(req, task_name):
    task = get_object_or_404(models.Quest, shortname=task_name)
    return open_task(req, task)


def answer_task(request, task):
    if not task.can_answer(request.user):
        return HttpResponseForbidden(_("You can't answer this task"))
    if request.method == 'POST':
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.quest_variant = task.get_variant(request.user)
            answer.save()
            return redirect(answer.get_absolute_url())
        else:
            return redirect(task.get_absolute_url())
    else:
        return redirect(task.get_absolute_url())


def answer_task_by_id(request, task_id):
    task = get_object_or_404(models.Quest, pk=task_id)
    return answer_task(request, task)


def answer_task_by_name(request, task_name):
    task = get_object_or_404(models.Quest, shortname=task_name)
    return answer_task(request, task)


def get_static(request, task, path):
    static = django.conf.settings.STATIC_URL.rstrip('/')
    new_path = '/'.join([static, 'taskstatic', task.shortname, task.get_hashkey, path])
    return redirect(new_path)


def get_task_static_by_id(request, task_id, path):
    task = get_object_or_404(models.Quest, pk=task_id)
    return get_static(request, task, path)


def get_task_static_by_name(request, task_name, path):
    task = get_object_or_404(models.Quest, shortname=task_name)
    return get_static(request, task, path)


def check_answer(request, answer_id):
    answer = get_object_or_404(models.QuestAnswer, pk=answer_id, quest_variant__team=request.user)
    return render(request, 'quests/show_answer.html', {'answer': answer})
