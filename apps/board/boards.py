from django.db.models import Sum, Count
from quests.models import Category, QuestAnswer
from teams.models import Team
from datetime import datetime
__author__ = 'Last G'


def get_task_board(team):
    tasks_by_category = Category.objects.order_by('order', 'quest__score').prefetch_related('quest_set', 'quest_set__open_for')
    for cat in tasks_by_category:
        for task in cat.quest_set.all():
            task.is_open = task.is_open_for(team)
            task.is_solved = task.is_solved_by(team)
    return tasks_by_category


scores_sql = """
select team.*, sum(answer.score) as score
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