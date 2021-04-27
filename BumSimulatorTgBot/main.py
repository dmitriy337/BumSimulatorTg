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

# keyboards.py
inline_btn_profile = InlineKeyboardButton('Герой', callback_data='Profile')
inline_btn_eat_happy = InlineKeyboardButton('Еда/Настроение', callback_data='Eat_Happy')
inline_btn_health = InlineKeyboardButton('Здороьве', callback_data='Health')
inline_btn_earn_money = InlineKeyboardButton('Зароботок', callback_data='EarnMoney')

inline_btn_BumWork = InlineKeyboardButton('Бродяжничество', callback_data='BumWork')
inline_btn_NormalWork = InlineKeyboardButton('Нормальная работа', callback_data='NormalWork')

menuKb = InlineKeyboardMarkup(row_width=3).add(inline_btn_profile)
menuKb.row(inline_btn_eat_happy, inline_btn_health)
menuKb.row(inline_btn_earn_money)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    responceMsg = await message.reply("Начинаю регистрацию...")
    await bot.send_chat_action(message.chat.id, types.ChatActions.TYPING)
    Services.RegisterNewUser(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
    await bot.send_message(message.chat.id, 'Зарегестрирован!')
    await asyncio.sleep(3)
    JsonR = Services.GetUserPersonage(message.chat.id)
    await bot.send_message(message.chat.id, Services.FormatUserToBeautifullMsg(JsonR), reply_markup=menuKb)


@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)

    if callback_query.data == 'Profile':
        JsonR = Services.GetUserPersonage(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, Services.FormatUserToBeautifullMsg(JsonR))

        
    elif callback_query.data == 'Eat_Happy':
        JsonR = Services.GetUserPersonage(callback_query.from_user.id)
        
        EatJson = Services.GetEat()
        HappyJson = Services.GetHappy() 
        resultJson = {"inline_keyboard": []}

        for eat_activity in EatJson['eat']:
            resultJson['inline_keyboard'].append([{"text":  f"{eat_activity['name']}\n{str(eat_activity['price'])}₽",
            "callback_data": f"{'eat_'+str(eat_activity['id'])}"}])


        await bot.send_message(callback_query.from_user.id, Services.FormatUserToBeautifullMsg(JsonR), reply_markup=resultJson)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    JsonR = Services.GetUserPersonage(msg.chat.id)
    await bot.send_message(msg.chat.id, Services.FormatUserToBeautifullMsg(JsonR), reply_markup=menuKb)


if __name__ == '__main__':
    executor.start_polling(dp)