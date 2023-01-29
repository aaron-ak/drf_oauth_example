from django.urls import path, include,re_path
from .views import *


app_name = 'REST'

urlpatterns = [
    path('v1/authenticate/google/', GoogleLogin.as_view(), name='google_login'),
    path('v1/users/', include('dj_rest_auth.urls')),
    path('v1/code', CodeView, name='code'),

]
