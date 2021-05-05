import Config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
from aiogram.types import *
import Services, asyncio

bot = Bot(token=Config.Token)
dp = Dispatcher(bot)

lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]




# Menu keyboards.py
inline_btn_profile = InlineKeyboardButton('Герой👨‍🦰', callback_data='btnM_Profile')
inline_btn_health = InlineKeyboardButton('Здоровье❤️', callback_data='btnM_Health')
inline_btn_eat = InlineKeyboardButton('Еда🍆', callback_data='btnM_Eat')
inline_btn_happy = InlineKeyboardButton('Счастье😁', callback_data='btnM_Happy')
inline_btn_earn_money = InlineKeyboardButton('Заработок💸', callback_data='btnM_EarnMoney')
menuKb = InlineKeyboardMarkup(row_width=3).add(inline_btn_profile)
menuKb.row(inline_btn_health, inline_btn_eat, inline_btn_happy, )
menuKb.row(inline_btn_earn_money)



inline_btn_BumWork = InlineKeyboardButton('Бродяжничество', callback_data='btnM_BumWork')
inline_btn_NormalWork = InlineKeyboardButton('Нормальная работа', callback_data='btnM_NormalWork')




@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    Msg = await  bot.send_message(message.chat.id,"Начинаю регистрацию...")
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)

    Services.RegisterNewUser(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)

    await Msg.edit_text('Зарегестрирован!')

    await asyncio.sleep(3)
    JsonR = Services.GetUserPersonage(message.chat.id)
    await bot.send_message(message.chat.id, Services.FormatUserToBeautifullMsg(JsonR), reply_markup=menuKb)


async def NotRegistered(userId):
    await bot.send_message(userId, "Вы не зарегестрированны\nОтправьте /start для регистрации))")


async def Вeath(userId):
    await bot.send_message(userId, "Ваша душа навсегда покидает это бренное тело бомжа, однако, вы всегда можете возродится в этом жестоком мире, в новой оболочке. Для начала отправьте /start")
    return 0


@dp.callback_query_handler(regexp='^btnM_')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if Services.GetUserPersonage(callback_query.from_user.id) == "NotRegistered":
        await NotRegistered(callback_query.from_user.id)
        return 0

    if callback_query.data == 'btnM_Profile':
        await callback_query.message.edit_text( Services.FormatUserProfileToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)))

        
    elif callback_query.data == 'btnM_Eat':
        resultJson = CreateEatMurkup()
        await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
         reply_markup=resultJson)
        
    
    elif callback_query.data == 'btnM_Happy':
        await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
         reply_markup=CreateHappyMurkup())

    elif callback_query.data == 'btnM_Health':
        resultJson = CreateHealthMurkup()
        await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
         reply_markup=resultJson)


@dp.callback_query_handler(regexp='^Menu')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if Services.GetUserPersonage(callback_query.from_user.id) == "NotRegistered":
        await NotRegistered(callback_query.from_user.id)
        return 0

    await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
         reply_markup=menuKb)



@dp.callback_query_handler(regexp='^eat_')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if Services.GetUserPersonage(callback_query.from_user.id) == "NotRegistered":
        await NotRegistered(callback_query.from_user.id)
        return 0

    executeResult = await Services.ExecuteEatActivity(eatId=callback_query.data.replace('eat_',''), userId=callback_query.from_user.id)
    if executeResult == 'NotHaveMoney':
        await bot.answer_callback_query(callback_query.id, text="Тебе не хватает денег на это))", show_alert=True)
    elif executeResult == 'Eat_die':
        await bot.answer_callback_query(callback_query.id, text="Ты помер с голоду)))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    elif executeResult == 'Health_die':
        await bot.answer_callback_query(callback_query.id, text="Ты помер)))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    elif executeResult == 'Happy_die':
        await bot.answer_callback_query(callback_query.id, text="Ты повесился))))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    else:
        await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
            reply_markup=CreateEatMurkup())

@dp.callback_query_handler(regexp='^happy_')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if Services.GetUserPersonage(callback_query.from_user.id) == "NotRegistered":
        await NotRegistered(callback_query.from_user.id)
        return 0

    executeResult = await Services.ExecuteHappyActivity(happyId=callback_query.data.replace('happy_',''), userId=callback_query.from_user.id)
    if executeResult == 'NotHaveMoney':
        await bot.answer_callback_query(callback_query.id, text="Тебе не хватает денег на это))", show_alert=True)
    elif executeResult == 'Eat_die':
        await bot.answer_callback_query(callback_query.id, text="Ты помер с голоду)))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    elif executeResult == 'Health_die':
        await bot.answer_callback_query(callback_query.id, text="Ты помер)))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    elif executeResult == 'Happy_die':
        await bot.answer_callback_query(callback_query.id, text="Ты повесился))))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    else:        
        await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
            reply_markup=CreateHappyMurkup())


@dp.callback_query_handler(regexp='^health_')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if Services.GetUserPersonage(callback_query.from_user.id) == "NotRegistered":
        await NotRegistered(callback_query.from_user.id)
        return 0

    executeResult = await Services.ExecuteHealthActivity(healthId=callback_query.data.replace('health_',''), userId=callback_query.from_user.id)

    if executeResult == 'NotHaveMoney':
        await bot.answer_callback_query(callback_query.id, text="Тебе не хватает денег на это)", show_alert=True)
    elif executeResult == 'Eat_die':
        await bot.answer_callback_query(callback_query.id, text="Ты помер с голоду)))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    elif executeResult == 'Health_die':
        await bot.answer_callback_query(callback_query.id, text="Ты помер)))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    elif executeResult == 'Happy_die':
        await bot.answer_callback_query(callback_query.id, text="Ты повесился))))", show_alert=True)
        await Вeath(callback_query.from_user.id)
    else:        
        await callback_query.message.edit_text(Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(callback_query.from_user.id)),
            reply_markup=CreateHealthMurkup())




def CreateEatMurkup():
    EatJson = Services.GetEat()
    resultJson = {"inline_keyboard": []}
    
    eatbtnsList=[]
    
    for eat_activity in EatJson['eat']:
        eatbtnsList.append({"text":  f"{eat_activity['name']}\n{str(eat_activity['price'])}₽",
        "callback_data": f"{'eat_'+str(eat_activity['id'])}"})


    resultJson['inline_keyboard'] = (lol(eatbtnsList, 2))
    resultJson['inline_keyboard'].append([{"text":"Назад","callback_data":"Menu"}])
    return resultJson

def CreateHappyMurkup():
    HappyJson = Services.GetHappy() 
    resultJson = {"inline_keyboard": []}

    happybtnsList=[]
    for eat_activity in HappyJson['happy']:
        happybtnsList.append({"text":  f"{eat_activity['name']}\n{str(eat_activity['price'])}₽",
        "callback_data": f"{'happy_'+str(eat_activity['id'])}"})

    resultJson['inline_keyboard']= (lol(happybtnsList, 2))
    resultJson['inline_keyboard'].append([{"text":"Назад","callback_data":"Menu"}])
    return resultJson

def CreateHealthMurkup():
    HappyJson = Services.GetHealth() 
    resultJson = {"inline_keyboard": []}

    healthbtnsList=[]
    for eat_activity in HappyJson['health']:
        healthbtnsList.append({"text":  f"{eat_activity['name']}\n{str(eat_activity['price'])}₽",
        "callback_data": f"{'health_'+str(eat_activity['id'])}"})

    resultJson['inline_keyboard'] = (lol(healthbtnsList, 2))
    resultJson['inline_keyboard'].append([{"text":"Назад","callback_data":"Menu"}])
    return resultJson


@dp.message_handler()
async def echo_message(msg: types.Message):
    if Services.GetUserPersonage(msg.from_user.id) == "NotRegistered":
        await NotRegistered(msg.from_user.id)
        return 0

    await bot.send_message(msg.chat.id, Services.FormatUserToBeautifullMsg(Services.GetUserPersonage(msg.chat.id)), reply_markup=menuKb)


if __name__ == '__main__':
    executor.start_polling(dp)