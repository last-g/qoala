# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import

from collections import defaultdict
from django.db.models import Sum, Count
import itertools
from operator import attrgetter
from quests.models import Category, QuestAnswer, Quest
from teams.models import Team
from datetime import datetime

__author__ = 'Last G'

board_sql = """
select quest.*, category.name as category_name ,
      sum(opens.team_id) as is_open , sum(answer.id) as is_solved,
      (
        select count(*) from quests_quest q2
        join quests_questvariant v2  on v2.quest_id = q2.id
        join quests_questanswer  a2 on a2.quest_variant_id = v2.id
        where
          a2.is_success and a2.is_checked
           and
          q2.id = quest.id
      ) as solutions_count
from quests_quest quest
 join quests_category category on quest.category_id = category.id
 left join quests_quest_open_for opens on opens.quest_id = quest.id and opens.team_id = %s
 left join quests_questvariant variant   on variant.quest_id = quest.id and variant.team_id = %s
 left join quests_questanswer  answer    on answer.quest_variant_id = variant.id and answer.is_checked and answer.is_success
group by quest.id, category.id
order by category.number, category.name, quest.score
"""

def groupby(collection, key):
    current = prev = object()
    res = []
    subres = []
    it = iter(collection)
    first = next(it)
    prev = getattr(first, key)
    subres.append(first)
    for el in it:
        current = getattr(el, key)
        if current == prev:
            subres.append(el)
        else:
            res.append((prev, subres))
            prev = current
            subres = [el]
    if subres:
        res.append((prev, subres))
    return res



def get_task_board(team):
    quests = list(Quest.objects.raw(board_sql, [team.id, team.id]))
    print(len(quests))
#    by_category = itertools.groupby(quests, attrgetter('category_name'))
#    by_category = defaultdict(list)
#    for q in quests:
#        by_category[q.category.name].append(q)
    by_category = groupby(quests, 'category_name')
    return by_category


scores_sql = """
select team.*, sum(COALESCE(answer.score,0)) as score
 from teams_team team
 left join quests_questvariant variant   on variant.team_id = team.id
-- left join quests_quest        quest     on quest.id = variant.quest_id
 left join quests_questanswer  answer    on answer.quest_variant_id = variant.id
 where
  (team.is_active and not team.is_staff and not team.is_superuser)
  and
  (
   (answer.is_checked and answer.is_success)
   or
   ( answer.id is null and answer.score is null )
  )
group by team.id
 order by score desc, max(answer.created_at)
"""


def scoreboard_modified(request, *args, **kwargs):
    try:
        time = QuestAnswer.objects.filter(is_checked=True, is_success=True).latest('created_at').created_at
        if time:
            return time
    except QuestAnswer.DoesNotExist:
        pass

    return datetime.now()


def get_scoreboard():
    answered = Team.objects.raw(scores_sql)
    return answered