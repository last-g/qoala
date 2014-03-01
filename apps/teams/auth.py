from .models import Team

__author__ = 'Last G'


class TokenAuthBackend(object):
    def authenticate(self, token=None):
        if token:
            return Team.objects.filter(token=token).first()
        return None

    def get_user(self, user_id, *args, **kwargs):
        try:
            return Team.objects.get(pk=user_id)
        except Team.DoesNotExist:
            return None