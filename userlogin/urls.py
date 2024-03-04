'''
urls file for the userlogin page
this page contains the link of application startup aka landing page
'''

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'user_login'),
]


