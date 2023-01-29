from django.shortcuts import render
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from rest_framework.decorators import api_view
from rest_framework.response import Response

import urllib.parse

class GoogleLogin(SocialLoginView):
# https://dj-rest-auth.readthedocs.io/en/latest/installation.html#social-authentication-optional
    class GoogleAdapter(GoogleOAuth2Adapter):
        access_token_url = "https://oauth2.googleapis.com/token"
        authorize_url = "https://accounts.google.com/o/oauth2/v2/auth"
        profile_url = "https://www.googleapis.com/oauth2/v2/userinfo"
    adapter_class = GoogleAdapter
    # Callback URL was used by mobile app
    callback_url = "http://localhost:8000/REST/v1/code"
    client_class = OAuth2Client


# Make testing easier
@api_view(['GET'])
def CodeView(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        code = urllib.parse.unquote(request.query_params['code'])
        return Response({
        	"code":code
        	})


