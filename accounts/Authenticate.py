from django.contrib.auth.backends import ModelBackend
import django.contrib.auth.models


class EmailBackend(ModelBackend):
    def authenticate(self, request, username, password):
        try:
            user = django.contrib.auth.models.User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                if user.check_password(password):
                    return user
        except:
            pass
        return None
