from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class DefaultUserBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        # Get the default user
        User = get_user_model()
        try:
            default_user = User.objects.get(username='admin2')
        except User.DoesNotExist:
            # Create a new superuser
            default_user = User.objects.create_superuser(
                username='admin2',
                email='admin2@example.com',
                password='mypassword'
            )
        return default_user

    def get_user(self, user_id):
        # Get the default user
        User = get_user_model()
        try:
            default_user = User.objects.get(username='admin2')
        except User.DoesNotExist:
            default_user = None
        return default_user