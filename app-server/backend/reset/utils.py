from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

def generate_auth_token():
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
    # Create an authentication token for the default user
    token, created = Token.objects.get_or_create(user=default_user)
    return token.key