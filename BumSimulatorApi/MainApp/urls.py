from django.urls import path, include
from .views import *


urlpatterns = [
    path('', GetAllUsers.as_view()),
]
