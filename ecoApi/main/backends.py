from django.contrib.auth.backends import BaseBackend
from .models import Usuario

class CNPJAuthBackend(BaseBackend):
    def authenticate(self, request, cnpj=None, password=None):
        user = self.authenticate_user(cnpj, password)
        return user

    def authenticate_user(self, cnpj, password):
        # Check if user is Usuario
        try:
            user = Usuario.objects.get(cnpj=cnpj)
            if user.check_password(password):
                return user
        except Usuario.DoesNotExist:
            pass


        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None
