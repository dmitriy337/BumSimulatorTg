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


class GetAllEat(APIView):
    def get(self, request):
        eats = Eat_activity.objects.all()
        serealizer = EatSerializer(eats, many=True)
        return Response(
            {'eat': serealizer.data}
        )


class GetAllHappy(APIView):
    def get(self, request):
        happies = Happy_activity.objects.all()
        serealizer = HappySerializer(happies, many=True)
        return Response(
            {'happy': serealizer.data}
        )


class GetAllHealth(APIView):
    def get(self, request):
        Health = Health_activity.objects.all()
        serealizer = HealthSerializer(Health, many=True)
        return Response(
            {'health': serealizer.data}
        )


class GetAllHouses(APIView):
    def get(self, request):
        house = Houses.objects.all()
        serealizer = HouseSerializer(house, many=True)
        return Response(
            {'houses': serealizer.data}
        )

class GetAllLearnings(APIView):
    def get(self, request):
        Learning = Learning_params.objects.all()
        serealizer = LearningSerializer(Learning, many=True)
        return Response(
            {'learnings': serealizer.data}
        )

class GetAllTransports(APIView):
    def get(self, request):
        transports = Transports.objects.all()
        serealizer = TransportSerializer(transports, many=True)
        return Response(
            {'transports': serealizer.data}
        )