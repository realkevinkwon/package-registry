from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class DefaultUserBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        # Get the default user
        User = get_user_model()
        default_user = User.objects.get(username='admin2')
        return default_user

    def get_user(self, user_id):
        # Get the default user
        User = get_user_model()
        default_user = User.objects.get(username='admin2')
        return default_user