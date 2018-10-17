from .utils import get_token_payload_with_jwk, get_first_email_from_payload
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

class IdTokenAuthentication(authentication.BaseAuthentication):
    
    def authenticate(self, request):
        # Get just the token from the authorization header ie Authorization: token xyz
        id_token = request.headers['Authorization'][6:end]
        if not id_token:
            return None
        payload = get_token_payload_with_jwk(token=id_token, nonce='DefaultNonce')
        email = get_first_email_from_payload(payload)
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)