from django.test import TestCase

from rest_framework.authtoken.models import Token

from django.test import Client

# self.user = Usuario.objects.create_user(
#     nome='test',
#     email='test@email.com',
#     password='test',
# )
# token, created = Token.objects.get_or_create(user=self.user)
# self.client = Client(HTTP_AUTHORIZATION='Token ' + token.key)