from django.conf.urls import url

from django.contrib import admin
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListView
    

    )

urlpatterns = [
    url('userlist', UserListView.as_view()),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
