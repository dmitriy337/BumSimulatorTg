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

    path('execute_eat_activity/eatId=<int:eatId>&userId=<int:userId>', ExecuteEatActivity.as_view()),

    path('execute_happy_activity/happyId=<int:happyId>&userId=<int:userId>', ExecuteHappyActivity.as_view()),
    path('execute_health_activity/healthId=<int:healthId>&userId=<int:userId>', ExecuteHealthActivity.as_view()),
]
