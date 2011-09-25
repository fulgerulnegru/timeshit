from django.contrib.auth.models import User
from django.core.validators import email_re

class EmailBackend:
    supports_inactive_user = False
    supports_object_permissions = False
    supports_anonymous_user = False

    def authenticate(self, email=None, password=None):
        #If username is an email address, then try to pull it up
        if email_re.search(email):
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return None
        else:
            return None
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


