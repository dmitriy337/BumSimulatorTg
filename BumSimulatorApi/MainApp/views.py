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


class Create_user(APIView):
    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()

        return Response({"success"})


class GetAll(APIView):
    def get(self, request):
        users = User.objects.all()
        serealizer = UserSerializer(users, many=True)
        return Response(
            {'users': serealizer.data}
        )