from django.db import models
from django.conf import settings
from django.db.models.aggregates import Max
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import os
import pickle
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.utils.translation import get_language
from datetime import timedelta
from django.utils.html import escape
from zope.cachedescriptors import property as zp
from django.utils.translation import ugettext as _
import qtils.models as qtils
import hashlib
from . import tasks

from qserver.quest import *

# Create your models here.
from teams.models import Team


def category_number():
    return Category.objects.aggregate(num=Max('number'))['num'] or 1


class Category(qtils.CreateAndUpdateDateMixin, models.Model):
    name = models.CharField(max_length=60)
    number = models.IntegerField(default=category_number)


@python_2_unicode_compatible
class Quest(qtils.CreateAndUpdateDateMixin, qtils.ModelDiffMixin, models.Model):
    """
    Quest model
    """
    shortname = models.CharField(max_length=60, unique=True)
    category = models.ForeignKey(Category, editable=False)
    score = models.IntegerField(blank=False, editable=False)

    provider_type = models.CharField(max_length=60, blank=True)
    provider_file = models.FilePathField(path=settings.TASKS_DIR, recursive=True, allow_folders=False, allow_files=True)
    provider_state = models.BinaryField(editable=False, null=True)
    provider_hash = models.CharField(max_length=60, editable=False)

    is_simple = models.BooleanField(_('Can be checked at main thread'), default=True, editable=True, blank=True)
    is_manual = models.BooleanField(_('Should be checked manually'), default=False, editable=True, blank=True)

    open_for = models.ManyToManyField('teams.Team', blank=True)

    @property
    def name(self):
        return self.provider.GetName()

    def _get_score(self):
        return int(self.provider.GetId().split(':')[1])

    @staticmethod
    def get_hash(file_path):
        block = 2 ** 20  # 1 Mb
        md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(block), b''):
                md5.update(chunk)
        return md5.hexdigest()

    def update_from_file(self, provider_type, provider_path):
        hashed = self.get_hash(provider_path)
        if hashed != self.provider_hash:
            provider = self.get_provider(provider_type, provider_path)
            (category, _) = Category.objects.get_or_create(name=provider.GetSeries())
            self.category = category
            self.score = self._get_score()
            self.provider_hash = hashed
            self.provider_state = pickle.dumps(provider)

    @staticmethod
    def get_provider(name, path):
        get_class = lambda x: globals()[x]
        ProviderClass = get_class(name)
        provider = ProviderClass(path)
        provider.dir = os.path.join(settings.TASKS_DATA_DIR, os.path.basename(path))  # XXX: Monkey patch
        return provider

    def is_open_for(self, team):
        return self.open_for.filter(pk=team.id).exists()

    @zp.Lazy
    def provider(self):
        if self.provider_state:
            return pickle.loads(self.provider_state)
        else:
            provider = self.get_provider(self.provider_type, self.provider_file)
            self.provider_state = pickle.dumps(provider)
            return provider

    def invalidate_variants(self):
        self.questvariant_set.update(is_valid=False)

    def _create_variant(self, team_id, try_count):
        provided_quest = self.provider.CreateQuest(team_id)
        timeout = timedelta(seconds=provided_quest.timeout) if provided_quest.timeout else timedelta(days=200)
        return QuestVariant.objects.create(
            quest_id=self.id,
            team_id=team_id,
            timeout=timezone.now() + timeout,
            try_count=try_count,
            state=pickle.dumps(provided_quest)
        )

    @property
    def get_hashkey(self):
        salt = settings.TASK_SALT
        key = salt + str(self.shortname)
        hasher = hashlib.md5()
        hasher.update(key)
        return hasher.hexdigest()


    def get_variant(self, team):
        team_id = team.id
        last_variant = self.questvariant_set.filter(team_id=team_id).order_by('try_count').first()
        if last_variant and last_variant.timeout < timezone.now() and last_variant.is_valid:
            return last_variant

        next_version = last_variant.try_count if last_variant else 1
        return self._create_variant(team_id, next_version)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse('quests.views.open_task_by_id', args=[str(self.id)])

    def is_solved_by(self, team):
        return self.questvariant_set.filter(questanswer__is_success=True, questanswer__is_checked=True).exists()

    def can_watch(self, team):
        return self.open_for.filter(pk=team.id).exists()

    def can_answer(self, team):
        return self.can_watch(team) and not self.is_solved_by(team)

    def __str__(self):
        return self.shortname

    class Meta(object):
        ordering = ['-score']


class QuestVariant(qtils.CreateAndUpdateDateMixin, models.Model):
    """
      Represent real quest variation for team, coz for different teams we could have different quest variations
    """
    quest = models.ForeignKey(Quest, null=False, blank=False)
    team = models.ForeignKey('teams.Team', null=False, blank=False)
    timeout = models.DateTimeField()
    try_count = models.IntegerField(default=1, null=False, blank=False)
    is_valid = models.BooleanField(default=True, null=False,
                                   blank=False)  # All question variants are invalidated, when new version of Question uploaded
    state = models.BinaryField()

    @property
    def html(self):
        return self.descriptor.raw_replace_patterns(self._get_html(), str(self.quest.id), str(self.team.id),
                                                    settings.TASK_SALT)

    @zp.Lazy
    def descriptor(self):
        return pickle.loads(self.state)


    @staticmethod
    def _get_with_lang(obj, lang):
        if not obj:
            return None
        lang = lang.lower()
        if type(obj) is dict:
            if lang in obj:
                return obj[lang]
            else:
                return None
        return obj

    def _get_content(self, lang):
        trans = self._get_with_lang(self.descriptor.html, lang)
        if trans:
            return trans
        else:
            trans = self._get_with_lang(self.descriptor.text, lang)
            if trans:
                return escape(trans)
            else:
                return None

    def _get_html(self):
        lang = get_language().lower()
        content = self._get_content(lang)
        if content:
            return content
        else:
            return self._get_content('en')

    # All fields

    def check(self, answer):
        return self.quest.provider.OnUserAction(self.descriptor, answer)


class QuestAnswer(qtils.CreateAndUpdateDateMixin, qtils.ModelDiffMixin, models.Model):
    """Model that describes someones try to score quest"""
    quest_variant = models.ForeignKey(QuestVariant, blank=False, null=False)
    is_checked = models.BooleanField(default=False, null=False, blank=False)

    is_success = models.BooleanField(default=False, null=False, blank=False)
    result = models.TextField(editable=True, blank=True, null=False)
    score = models.IntegerField(default=0, null=False, blank=False)

    answer = models.TextField()
    answer_file = models.FileField(upload_to="media", editable=False)

    def check(self):
        status, message = self.quest_variant.check(self.answer)
        self.is_checked = True
        self.is_success = status
        self.result = message
        self.score = self.quest_variant.quest.score
        self.save()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse('quests.views.check_answer', args=[self.id])


@receiver(post_save, sender=QuestAnswer)
def check_answer(sender, instance, created, **kwargs):
    answer = instance
    quest = answer.quest_variant.quest
    if created and not quest.is_manual and not answer.is_checked:
        if quest.is_simple and False:
            tasks.check_answer(answer)
        else:
            tasks.check_answer.delay(answer)


def determ_profire_type(provider_file):
    from os.path import basename, splitext

    root, ext = splitext(basename(provider_file))
    if ext.lower() == '.xml':
        return 'XMLQuestProvider'
    else:
        return 'ScriptQuestProvider'


@receiver(pre_save, sender=Quest)
def update_default(sender, instance, **kwargs):
    quest = instance
    if not quest.provider_type:
        quest.provider_type = determ_profire_type(quest.provider_file)


@receiver(pre_save, sender=Quest)
def load_initial(sender, instance, **kwargs):
    quest = instance
    if quest.pk is None or quest.get_field_diff('provider_file'):
        quest.update_from_file(quest.provider_type, quest.provider_file)


@receiver(post_save, sender=Quest)
def invalidate_variants(sender, instance, **kwargs):
    quest = instance
    if quest.get_field_diff('provider_hash'):
        quest.invalidate_variants()


@receiver(post_save, sender=QuestAnswer)
def open_quests(sender, instance, **kwargs):
    answer = instance
    if answer.is_checked and answer.is_success and (
                answer.get_field_diff('is_checked') or answer.get_field_diff('is_success')):
        quest = answer.quest_variant.quest
        category = quest.category
        score = quest.score
        all_teams = list(Team.objects.all())
        nxt = Quest.objects.filter(category=category, score__gt=score).order_by('score').first()
        if nxt:
            nxt.open_for.add(*all_teams)