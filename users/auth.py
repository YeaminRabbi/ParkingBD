from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class Email_or_Username(BaseBackend):
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
    def authenticate(self, request, username=None, password=None, **kwargs):
        # UserModel = get_user_model()
        try:
            user = get_user_model().objects.get(Q(username__exact=username) | Q(email__exact=username))
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None
        return None