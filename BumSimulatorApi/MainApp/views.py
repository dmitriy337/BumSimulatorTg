import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import *
from  .serializers import *
import random


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

class GetAllNormalWork(APIView):
    def get(self, request):
        eats = NormalWorks.objects.all()
        serealizer = NormalWorkSerializer(eats, many=True)
        return Response(
            {'normal_work': serealizer.data}
        )

class GetAllPersonageWork(APIView):
    def get(self, request):
        eats = PersonageWorks.objects.all()
        serealizer = PersonageWorkSerializer(eats, many=True)
        return Response(
            {'personage_work': serealizer.data}
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

class ExecuteEatActivity(APIView):
    def get(self, request, eatId, userId):

        eat: Eat_activity = get_object_or_404(Eat_activity.objects.all(), id=eatId)

        user: User = get_object_or_404(User.objects.all(), Id=userId)

        character: Personage =  Personage.objects.get(id=user.Character.id)

        # Validate eat
        if eat.howMuchEatMin < eat.howMuchEatMax:
            addEat = random.randint(eat.howMuchEatMin, eat.howMuchEatMax)
        else:
            addEat = random.randint(eat.howMuchEatMax, eat.howMuchEatMin)
        if (character.eat_level + addEat) >= 100:
            character.eat_level = 100
        elif (character.eat_level + addEat) <= 0:
            character.eat_level = 0
        else:
            character.eat_level += addEat

        #Validate health
        if eat.howMuchHealthMin < eat.howMuchHealthMax:
            addHealth = random.randint(eat.howMuchHealthMin, eat.howMuchHealthMax)
        else:
            addHealth = random.randint(eat.howMuchHealthMax, eat.howMuchHealthMin)
        if (character.health_level + addHealth) >= 100:
            character.health_level = 100
        elif (character.health_level + addHealth) <= 0:
            character.health_level = 0
        else:
            character.health_level += addHealth

        #Validate happy
        if eat.howMuchHappyMin < eat.howMuchHappyMax:
            addHappy = random.randint(eat.howMuchHappyMin, eat.howMuchHappyMax)
        else:
            addHappy = random.randint(eat.howMuchHappyMax, eat.howMuchHappyMin)
        if (character.happy_level + addHappy) >= 100:
            character.happy_level = 100
        elif (character.happy_level + addHappy) <= 0:
            character.happy_level = 0
        else:
            character.happy_level +=  addHappy

        character.save()
        user.save()
        serealizer = UserSerializer(user, many=False)
        return Response(
            {'user': serealizer.data}
        )

class ExecuteHappyActivity(APIView):
    def get(self, request, happyId, userId):
        happy: Happy_activity = get_object_or_404(Happy_activity.objects.all(), id=happyId)
        user: User = get_object_or_404(User.objects.all(), Id=userId)
        character: Personage =  Personage.objects.get(id=user.Character.id)

        #Validate eat
        if happy.howMuchEatMin < happy.howMuchEatMax:
            addEat = random.randint(happy.howMuchEatMin, happy.howMuchEatMax)
        else:
            addEat = random.randint(happy.howMuchEatMax, happy.howMuchEatMin)
        if (character.eat_level + addEat) >= 100:
            character.eat_level = 100
        elif (character.eat_level + addEat) <= 0:
            character.eat_level = 0
        else:
            character.eat_level += addEat

        #Validate health
        if happy.howMuchHealthMin < happy.howMuchHealthMax:
            addHealth = random.randint(happy.howMuchHealthMin, happy.howMuchHealthMax)
        else:
            addHealth = random.randint(happy.howMuchHealthMax, happy.howMuchHealthMin)

        if (character.health_level + addHealth) >= 100:
            character.health_level = 100
        elif (character.health_level + addHealth) <= 0:
            character.health_level = 0
        else:
            character.health_level += addHealth

        #Validate happy
        if happy.howMuchHappyMin < happy.howMuchHappyMax:
            addHappy = random.randint(happy.howMuchHappyMin, happy.howMuchHappyMax)
        else:
            addHappy = random.randint(happy.howMuchHappyMax, happy.howMuchHappyMin)
        if (character.happy_level + addHappy) >= 100:
            character.happy_level = 100
        elif (character.happy_level + addHappy) <= 0:
            character.happy_level = 0
        else:
            character.happy_level +=  addHappy

        character.save()
        user.save()

        serealizer = UserSerializer(user, many=False)
        return Response(
            {'user': serealizer.data}
        )


class ExecuteHealthActivity(APIView):
    def get(self, request, healthId, userId):
        health: Health_activity = get_object_or_404(Health_activity.objects.all(), id=healthId)
        user: User = get_object_or_404(User.objects.all(), Id=userId)
        character: Personage =  Personage.objects.get(id=user.Character.id)

        #Validate eat
        if health.howMuchEatMin < health.howMuchEatMax:
            addEat = random.randint(health.howMuchEatMin, health.howMuchEatMax)
        else:
            addEat = random.randint(health.howMuchEatMax, health.howMuchEatMin)
        if (character.eat_level + addEat) >= 100:
            character.eat_level = 100
        elif (character.eat_level + addEat) <= 0:
            character.eat_level = 0
        else:
            character.eat_level += addEat

        #Validate health
        if health.howMuchHealthMin < health.howMuchHealthMax:
            addHealth = random.randint(health.howMuchHealthMin, health.howMuchHealthMax)
        else:
            addHealth = random.randint(health.howMuchHealthMax, health.howMuchHealthMin)

        if (character.health_level + addHealth) >= 100:
            character.health_level = 100
        elif (character.health_level + addHealth) <= 0:
            character.health_level = 0
        else:
            character.health_level += addHealth

        #Validate happy
        if health.howMuchHappyMin < health.howMuchHappyMax:
            addHappy = random.randint(health.howMuchHappyMin, health.howMuchHappyMax)
        else:
            addHappy = random.randint(health.howMuchHappyMax, health.howMuchHappyMin)
        if (character.happy_level + addHappy) >= 100:
            character.happy_level = 100
        elif (character.happy_level + addHappy) <= 0:
            character.happy_level = 0
        else:
            character.happy_level +=  addHappy

        character.save()
        user.save()

        serealizer = UserSerializer(user, many=False)
        return Response(
            {'user': serealizer.data}
        )



class ExecutePersonageWorks(APIView):
    def get(self, request, personageWorkId, userId):
        personageWorks: PersonageWorks = get_object_or_404(PersonageWorks.objects.all(), id=personageWorkId)

        user: User = get_object_or_404(User.objects.all(), Id=userId)
        character: Personage = Personage.objects.get(id=user.Character.id)

        if character.rating < personageWorks.unlockRating:
            return Response(
                {'RatingError'}
            )

        # Validate eat
        if personageWorks.howMuchEatMin < personageWorks.howMuchEatMax:
            addEat = random.randint(personageWorks.howMuchEatMin, personageWorks.howMuchEatMax)
        else:
            addEat = random.randint(personageWorks.howMuchEatMax, personageWorks.howMuchEatMin)
        if (character.eat_level + addEat) >= 100:
            character.eat_level = 100
        elif (character.eat_level + addEat) <= 0:
            character.eat_level = 0
        else:
            character.eat_level += addEat

        # Validate health
        if personageWorks.howMuchHealthMin < personageWorks.howMuchHealthMax:
            addHealth = random.randint(personageWorks.howMuchHealthMin, personageWorks.howMuchHealthMax)
        else:
            addHealth = random.randint(personageWorks.howMuchHealthMax, personageWorks.howMuchHealthMin)

        if (character.health_level + addHealth) >= 100:
            character.health_level = 100
        elif (character.health_level + addHealth) <= 0:
            character.health_level = 0
        else:
            character.health_level += addHealth

        # Validate happy
        if personageWorks.howMuchHappyMin < personageWorks.howMuchHappyMax:
            addHappy = random.randint(personageWorks.howMuchHappyMin, personageWorks.howMuchHappyMax)
        else:
            addHappy = random.randint(personageWorks.howMuchHappyMax, personageWorks.howMuchHappyMin)
        if (character.happy_level + addHappy) >= 100:
            character.happy_level = 100
        elif (character.happy_level + addHappy) <= 0:
            character.happy_level = 0
        else:
            character.happy_level += addHappy


        if personageWorks.HowMuchEarningsMin < personageWorks.HowMuchEarningsMax:
            addEarnings = random.randint(personageWorks.HowMuchEarningsMin, personageWorks.HowMuchEarningsMax)
        else:
            addEarnings = random.randint(personageWorks.HowMuchEarningsMax, personageWorks.HowMuchEarningsMin)

        character.money += addEarnings

        if personageWorks.HowMuchEarningsItemsMin < personageWorks.HowMuchEarningsItemsMax:
            addEarningItems = random.randint(personageWorks.HowMuchEarningsItemsMin, personageWorks.HowMuchEarningsItemsMax)
        else:
            addEarningItems = random.randint(personageWorks.HowMuchEarningsItemsMax, personageWorks.HowMuchEarningsItemsMin)

        character.items += addEarningItems
        addRating = random.randint(personageWorks.howMuchRatingMin, personageWorks.howMuchRatingMax)
        character.rating += addRating
        character.save()
        user.save()

        serealizer = UserSerializer(user, many=False)
        return Response(
            {'user': serealizer.data}
        )



class ExecuteNormalWorks(APIView):
    def get(self, request, normalWorkId, userId):
        personageWorks: NormalWorks = get_object_or_404(NormalWorks.objects.all(), id=personageWorkId)

        user: User = get_object_or_404(User.objects.all(), Id=userId)
        character: Personage = Personage.objects.get(id=user.Character.id)

        if character.rating < personageWorks.unlockRating:
            return Response(
                {'RatingError'}
            )

        # Validate eat
        if personageWorks.howMuchEatMin < personageWorks.howMuchEatMax:
            addEat = random.randint(personageWorks.howMuchEatMin, personageWorks.howMuchEatMax)
        else:
            addEat = random.randint(personageWorks.howMuchEatMax, personageWorks.howMuchEatMin)
        if (character.eat_level + addEat) >= 100:
            character.eat_level = 100
        elif (character.eat_level + addEat) <= 0:
            character.eat_level = 0
        else:
            character.eat_level += addEat

        # Validate health
        if personageWorks.howMuchHealthMin < personageWorks.howMuchHealthMax:
            addHealth = random.randint(personageWorks.howMuchHealthMin, personageWorks.howMuchHealthMax)
        else:
            addHealth = random.randint(personageWorks.howMuchHealthMax, personageWorks.howMuchHealthMin)

        if (character.health_level + addHealth) >= 100:
            character.health_level = 100
        elif (character.health_level + addHealth) <= 0:
            character.health_level = 0
        else:
            character.health_level += addHealth

        # Validate happy
        if personageWorks.howMuchHappyMin < personageWorks.howMuchHappyMax:
            addHappy = random.randint(personageWorks.howMuchHappyMin, personageWorks.howMuchHappyMax)
        else:
            addHappy = random.randint(personageWorks.howMuchHappyMax, personageWorks.howMuchHappyMin)
        if (character.happy_level + addHappy) >= 100:
            character.happy_level = 100
        elif (character.happy_level + addHappy) <= 0:
            character.happy_level = 0
        else:
            character.happy_level += addHappy


        if personageWorks.HowMuchEarningsMin < personageWorks.HowMuchEarningsMax:
            addEarnings = random.randint(personageWorks.HowMuchEarningsMin, personageWorks.HowMuchEarningsMax)
        else:
            addEarnings = random.randint(personageWorks.HowMuchEarningsMax, personageWorks.HowMuchEarningsMin)

        character.money += addEarnings

        if personageWorks.HowMuchEarningsItemsMin < personageWorks.HowMuchEarningsItemsMax:
            addEarningItems = random.randint(personageWorks.HowMuchEarningsItemsMin, personageWorks.HowMuchEarningsItemsMax)
        else:
            addEarningItems = random.randint(personageWorks.HowMuchEarningsItemsMax, personageWorks.HowMuchEarningsItemsMin)

        character.items += addEarningItems

        addRating = random.randint(personageWorks.howMuchRatingMin, personageWorks.howMuchRatingMax)
        character.rating += addRating

        character.save()
        user.save()

        serealizer = UserSerializer(user, many=False)
        return Response(
            {'user': serealizer.data}
        )
