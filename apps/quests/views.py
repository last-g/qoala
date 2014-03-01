import django
from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.template import response
from django.utils.translation import ugettext as _
from . import models
from . import forms


# Create your views here.


def open_task(req, task_id):
    task = get_object_or_404(models.Quest, pk=task_id)
    if not task.is_open_for(req.user):
        return HttpResponseForbidden(_("This task is closed for you"))

    variant = task.get_variant(req.user)
    return render(req, 'quests/open.html', {'variant': variant, 'form': forms.AnswerForm()})


def answer_task(request, task_id):
    task = get_object_or_404(models.Quest, pk=task_id)
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


def check_answer(request, answer_id):
    answer = get_object_or_404(models.QuestAnswer, pk=answer_id, quest_variant__team=request.user)
    return render(request, 'quests/show_answer.html', {'answer': answer})
