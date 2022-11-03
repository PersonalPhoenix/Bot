from email import header, message
from encodings import utf_8, utf_8_sig
from pickle import NONE
from pyexpat import native_encoding
from secrets import choice
from aiogram import Bot, Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup
import lxml
import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.markdown import hlink
import random


#Задаем переменную бота для обращения в телегу по токену / Create token
TOKEN = None #Обозначаем токен / Denote token
with open("C:/Users/applm/OneDrive/Рабочий стол/Projects/project BOT/TOKEN.txt") as f:  #Открываем файл с токеном / Open file with token
    TOKEN = f.read().strip() #Считываем токен и удаляем лишнее / Read and delete excess

bot = Bot (TOKEN, parse_mode=types.ParseMode.HTML) #Присваиваем токен / Assigning a token


#Словарь для парсинга / Dictionary for parse
news_dict = {}


#Dp = диспетчер для комманд / Dispatcherfor command
dp = Dispatcher (bot)


#Клава / Keyboard
news_key = KeyboardButton('/news') #Создаем кнопку / Create button
news_last = KeyboardButton('/last') #Создаем кнопку / Create button
cats = KeyboardButton("/kitty 🦊") #Создаем кнопку / Create button
ti = KeyboardButton ("/TI11") #Создаем кнопку / Create button
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(news_key,news_last,ti,cats) #Выводи клавиатуру с кнопками / Output keyboard with buttons


#Подклава для китиков / Sub keyboard for kitty
cats_animation = KeyboardButton('/flex_kitty 🐈') #Создаем кнопку / Create button
cats_picture = KeyboardButton('/tomcat 😼') #Создаем кнопку / Create button
back = KeyboardButton('/back ❌') #Создаем кнопку / Create button
catsMenu = ReplyKeyboardMarkup (resize_keyboard=True).row(back,cats_animation,cats_picture) #Возвращаемся из под клавы в глав клаву / Return main keyboard from sub keyborad


#Сообщение в CMD о старте / Message about start in CMD
async def on_startup (_): #Задаем функцию / Setting the function
    print ("МУЗЫКА ПОШЛА") #Вывод сообщения / Output message


#Комманда старта / Command start
@dp.message_handler (commands = ["start"]) #Задаем комманду / Setting the command
async def start  (message: types.Message): #Задаем функцию / Setting the function
    await bot.send_message( message.from_user.id, 'YEP начинаем',reply_markup = mainMenu) #Отправляем приветствие / Send hello
    await bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEFiWli9TsP9B1BLa8HrEqL51EtH4UQEAACnhYAArpIyUtcjAeK6Rs_SykE") #Отправляем стикер / Send sticker


#Парсер с выводом / Parse with output
@dp.message_handler (commands=["news"]) 
async def news (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.cybersport.ru/tags/dota-2")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find_all (class_="rounded-block root_d51Rr with-hover no-padding no-margin")
    for round in rounded_block:
        round_title = round.find (class_="title_nSS03").text
        round_data = round.find (class_="pub_AKjdn").text
        round_link = round.find (class_="link_CocWY")
        round_url = f'https://www.cybersport.ru{round_link.get("href")}'
        news_dict [round_data] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("news_dict.json","w",encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(news_dict.items()):
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)


#Вывод последней новости на данный момент / Output a last news at moment
@dp.message_handler(commands=["last"])
async def news (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.cybersport.ru/tags/dota-2")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find_all (class_="rounded-block root_d51Rr with-hover no-padding no-margin")
    for round in rounded_block:
        round_title = round.find (class_="title_nSS03").text
        round_data = round.find (class_="pub_AKjdn").text
        round_link = round.find (class_="link_CocWY")
        round_url = f'https://www.cybersport.ru{round_link.get("href")}'
        news_dict [round_data] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("news_dict.json","w",encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(news_dict.items())[-1:]:
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)
    

#Cписок id стикеров статичных котов / List id stickers static cats
kit = ["CAACAgIAAxkBAAEGReBjYN1bncaxE0k4O8yqWpHidwq-QQADFwACBud5SAZAQLkOAjyhKgQ", #CATS
"CAACAgIAAxkBAAEF9I9jNd9ItkiG4oztiyly1n3Z0jD8SAACIwADezwGEa6cmphaatyTKgQ",
"CAACAgIAAxkBAAEGReZjYN23Pp7-EJ9uxQbGg1r0mLThsAACRhAAAnN6CUt9kgUt0XU89ioE",
"CAACAgIAAxkBAAEGRehjYN3B63RU0TqbkSlFW0vdW4ZPfAACjg8AApdNCUsYXNqjioE8WioE",
"CAACAgIAAxkBAAEGRepjYN3Df_-tKfuSL5pddAcfmsETrgACEg0AAunxCUvhn1Q5qy-GUSoE",
"CAACAgIAAxkBAAEGRexjYN3RTz_FNU_mX17K-GMiVSPluQACLg8AAqswCEsreRP3r0AjwioE",
"CAACAgIAAxkBAAEGRe1jYN3RP-lLL4qb-5wrvhM-xd5-wQACrAwAAim2CUsgawABJJBx8_sqBA",
"CAACAgIAAxkBAAEGRfBjYN3TK7LxnWJ4sGF4clFC0Ej4GwAC_AwAAmn2CUunISFcu6AR3yoE"]

#список id стикеров флексящих котов / List id stikers flex cats
flex = ["CAACAgIAAxkBAAEFkWti-oEXVf1fIkJDQjvMjDt2WyAZ1wACNBcAAkOaoEhNfT8fIoHPmCkE", #FLEX
"CAACAgIAAxkBAAEGRdBjYN0J4YyYdPS6O1PIY6ZqRX1vhAACoxwAAiK_oEhAt_ZmqiP8iCoE",
"CAACAgIAAxkBAAEGRdFjYN0KL1u7uPzOAAGLYZDrPkTuSgoAAooTAAJMKKhIU9jSLbNMSMsqBA",
"CAACAgIAAxkBAAEGRdJjYN0KzVXO-VoJhyObdplZgxb3TwACVxUAAoTs6UhuQVQZpoVpASoE",
"CAACAgIAAxkBAAEGRdZjYN02Htlvpp3v5l2h6I50KM-iwgACixgAAin9qUixIZgpBYJiLCoE",
"CAACAgIAAxkBAAEGRdpjYN1JeEA53XKLWhgOwDQhtylUjgACihMAAjSNSUirTNDsAVVtjSoE",
"CAACAgIAAxkBAAEGRdxjYN1UTKGlQhN8E2MLwzeU9Bbu5gACZRYAAq8SCUjHYG0TMAAB5-4qBA",
"CAACAgIAAxkBAAEGRd5jYN1Z98oRRs3rbbIAAYoN6juyUdwAAk4YAAJPp9BL5qYnFJhB_RwqBA",
"CAACAgIAAxkBAAEGReRjYN2UUuk4qPEw7A7EwR0_Sf_WWwACKhcAAu_jyEvWhp-EtkEyvioE"]

#Клавиатуры киттиков / Kitty keyboard
@dp.message_handler()
async def kitty (message):       
    if message.text == "/kitty 🦊":
        await bot.send_message( message.from_user.id, 'Выбери какого котика ты хочешь',reply_markup = catsMenu)
    if message.text == "/flex_kitty 🐈":
        await bot.send_sticker(message.chat.id,choice(flex))
    elif message.text == "/tomcat 😼":
        await bot.send_sticker(message.chat.id,choice(kit))
    elif message.text == '/back ❌':
        await bot.send_message(message.from_user.id,"Вернемся к делу",reply_markup = mainMenu)
    elif message.text == "/TI11":
        await bot.send_message(message.from_user.id,"""The Intenational 11 проходил в Сингпуре. 
Дата проведения 15.10.2022 - 30.10.2022. 
Победителем по результатам игр стал европейский коллектив Tundra Esports""")

#запуск бота  
if __name__ == "__main__":
    executor.start_polling (dp, skip_updates=True, on_startup=on_startup)
