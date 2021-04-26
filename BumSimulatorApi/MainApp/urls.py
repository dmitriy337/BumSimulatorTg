from django.urls import path, include
from .views import *


urlpatterns = [
    path('get_users', GetAllUsers.as_view()),
    path('create_user', Create_user.as_view()),
]
