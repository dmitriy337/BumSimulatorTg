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
    return j


def FormatUserToBeautifullMsg(usr: json):
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



