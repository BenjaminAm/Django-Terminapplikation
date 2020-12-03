from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from base64 import b64encode
from requests import get


class StudipAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        User = get_user_model()
        url = 'https://studip.uni-osnabrueck.de/api.php/user/'
        auth64 = b64encode((username + ":" + password).encode("ascii"))
        auth64 = auth64.decode("ascii")
        headers = {
            'Content-Type': 'text/json',
            'Authorization': 'Basic ' + auth64,
        }
        r = get(url, headers=headers)
        if r.status_code == 200:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                user = User(username=username)
                user.save()
            return user
        return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None