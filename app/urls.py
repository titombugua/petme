from django.conf.urls import url,include
from rest_framework import routers

from django.contrib import admin
from . import views
from app import views
from .views import *
	

# from .views import (
# 	post_list,
# 	post_create,
# 	post_detail,
# 	post_update,
# 	post_delete,
# 	)

urlpatterns = [
	# url(r'^$', post_list, name='list'),
    # url(r'^create/$', post_create),
    # url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
