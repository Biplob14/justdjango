from os import name
from django.contrib import admin
from django.urls import path, include
# from core.views import TestView
from core.views import PostView, PostCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name='test'),
    path('create/', PostCreateView.as_view(), name='test'),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    # shows the reserverd token
    path('api/token', obtain_auth_token, name='obtain-token')
]
