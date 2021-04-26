from django.urls import path, include
from .views import *


urlpatterns = [
    path('get_users', GetAllUsers.as_view()),
    path('create_user', Create_user.as_view()),
    path('get_eat', GetAllEat.as_view()),
    path('get_happy', GetAllHappy.as_view()),
    path('get_health', GetAllHealth.as_view()),
    path('get_houses', GetAllHouses.as_view()),
    path('get_learnings', GetAllLearnings.as_view()),
    path('get_transports', GetAllTransports.as_view()),
]
