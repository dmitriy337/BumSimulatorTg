from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from  .serializers import *


class GetAllUsers(APIView):

    def get(self, request):
        users = User.objects.all()
        serealizer = UserSerializer(users, many=True)
        return Response(
            {'users': serealizer.data}
        )