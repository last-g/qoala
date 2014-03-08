from django.db.models.aggregates import Count
from django.shortcuts import render
from django.views.decorators.http import condition
from quests.models import Quest, Category
from .boards import *
# Create your views here.
from teams.models import Team


def task_board(request):
    tasks_by_category = get_task_board(request.user)
    return render(request, 'board/taskboard.html', {'by_categories': tasks_by_category})


#@condition(last_modified_func=scoreboard_modified)
def score_board(request):
    scores = get_scoreboard()
    return render(request, 'board/scoreboard.html', {'teams': scores})