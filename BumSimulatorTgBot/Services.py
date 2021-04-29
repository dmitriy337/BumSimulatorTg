import requests, json
from aiogram.types import *


def RegisterNewUser(userId, Username: str, FirstName: str, LastName: str) -> bool:
    data = {
        "user": {
            "Id": userId,
            "Username": f"{Username}",
            "Firstname": f"{FirstName}",
            "LastName": f"{LastName}"
            }
    }
    r = requests.post('http://vuhiza.hopto.org:8080/api/create_user', json=data)
    print(r.content)


def GetUserPersonage(userId: int,) -> json:
    r = requests.get(f'http://vuhiza.hopto.org:8080/api/get_user/userId={userId}')
    j = json.loads(r.content.decode('utf-8'))
    if r.content.decode('utf-8').count('Not found') > 0:
        return "NotRegistered"
    return j


def FormatUserToBeautifullMsg(usr: json):
    resultString = ''
    if usr['user']:
        Character = usr['user']['Character']
        resultString += '💸Money: '+str(Character['money'])+'  '
        resultString += '🍾Bottles: '+str(Character['items'])+'\n'
        resultString += '❤️Health: '+str(Character['health_level'])+'/100'+'  ' 
        resultString += '🍆Eat: '+str(Character['eat_level'])+'/100'+'\n'
        resultString += '😁Happy: '+str(Character['happy_level'])+'/100'+'\n'
    return resultString


def FormatUserProfileToBeautifullMsg(usr: json):
    resultString = ''
    if usr['user']:
        Character = usr['user']['Character']
        resultString += 'Age: '+str(Character['age'])+'\n'
        resultString += 'Money: '+str(Character['money'])+'\n'
        resultString += 'Bottles: '+str(Character['items'])+'\n'
        resultString += 'Rating: '+str(Character['rating'])+'\n'
        resultString += 'Health: '+str(Character['health_level'])+'\n'
        resultString += 'Eat: '+str(Character['eat_level'])+'\n'
        resultString += 'Happy: '+str(Character['happy_level'])+'\n'
    return resultString


def GetEat():
    r = requests.get(f'http://vuhiza.hopto.org:8080/api/get_eat')
    j = json.loads(r.content.decode('utf-8'))
    return j

def GetHappy():
    r = requests.get(f'http://vuhiza.hopto.org:8080/api/get_happy')
    j = json.loads(r.content.decode('utf-8'))
    return j

def GetHealth():
    r = requests.get(f'http://vuhiza.hopto.org:8080/api/get_health')
    j = json.loads(r.content.decode('utf-8'))
    return j


async def ExecuteEatActivity(eatId: int, userId: int,) -> json:
    r =  requests.get(f'http://vuhiza.hopto.org:8080/api/execute_eat_activity/eatId={eatId}&userId={userId}')
    if r.content.decode('utf-8').count('not_enought_money') > 0:
        return 'NotHaveMoney'
    if r.content.decode('utf-8').count('Eat_die') > 0:
        return 'Eat_die'
    if r.content.decode('utf-8').count('Health_die') > 0:
        return 'Health_die'
    if r.content.decode('utf-8').count('Happy_die') > 0:
        return 'Happy_die'



async def ExecuteHealthActivity(healthId: int, userId: int,):
    r = requests.get(f'http://vuhiza.hopto.org:8080/api/execute_health_activity/healthId={healthId}&userId={userId}')
    if r.content.decode('utf-8').count('not_enought_money') > 0:
        return 'NotHaveMoney'
    if r.content.decode('utf-8').count('Eat_die') > 0:
        return 'Eat_die'
    if r.content.decode('utf-8').count('Health_die') > 0:
        return 'Health_die'
    if r.content.decode('utf-8').count('Happy_die') > 0:
        return 'Happy_die'


async def ExecuteHappyActivity(happyId: int, userId: int,) -> json:
    r = requests.get(f'http://vuhiza.hopto.org:8080/api/execute_happy_activity/happyId={happyId}&userId={userId}')
    if r.content.decode('utf-8').count('not_enought_money') > 0:
        return 'NotHaveMoney'
    if r.content.decode('utf-8').count('Eat_die') > 0:
        return 'Eat_die'
    if r.content.decode('utf-8').count('Health_die') > 0:
        return 'Health_die'
    if r.content.decode('utf-8').count('Happy_die') > 0:
        return 'Happy_die'
