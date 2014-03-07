from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import query
from django.utils.translation import ugettext as _

# Create your models here.


class TeamQuerySet(query.QuerySet):
    def with_score(self):
        return self.values('name').filter().annotate(score=models.Sum('questvariant__questanswer__score'))


class TeamManager(BaseUserManager):
    def get_queryset(self):
        return TeamQuerySet(self.model)

    def with_score(self):
        return self.get_queryset().with_score()

    def create_user(self, *args, **kwargs):
        self.create_team(*args, **kwargs)

    def create_superuser(self, *args, **kwargs):
        self.create_team(is_staff=True, is_superuser=True, *args, **kwargs)

    def create_team(self, name, password=None, is_staff=False, is_superuser=False):
        if not name:
            raise ValueError("Team must have nonempty name")

        team = self.model(name=name, is_staff=is_staff, is_superuser=is_superuser)
        team.set_password(password)
        team.save(using=self._db)
        return team


class Team(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=60, help_text=_("team name"), blank=False, null=False, unique=True, db_index=True)
    is_staff = models.BooleanField(help_text=_('staff status'), blank=False, null=False, default=False, db_index=True)
    is_active = models.BooleanField(help_text=_('User can log in'), blank=False, null=False, default=True, db_index=True)
    token = models.CharField(max_length=64, unique=True, blank=False, null=True, db_index=True)

    USERNAME_FIELD = 'name'

    objects = TeamManager()

    @property
    def get_full_name(self):
        return self.name

    @property
    def get_short_name(self):
        return self.name

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('teams.views.show', args=[self.name])