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


""" -----------------------------------------------------------------------------------------------------------------------------------"""


#Задаем переменную бота для обращения в телегу по токену / Create token
TOKEN = None #Обозначаем токен / Denote token
with open("C:/Users/applm/OneDrive/Рабочий стол/Projects/project BOT/TOKEN.txt") as f:  #Открываем файл с токеном / Open file with token
    TOKEN = f.read().strip() #Считываем токен и удаляем лишнее / Read and delete excess

bot = Bot (TOKEN, parse_mode=types.ParseMode.HTML) #Присваиваем токен / Assigning a token

#Словари для парсинга / Dictionary for parse

#Новости киберспорта
Dnews_dict = {}
CSnews_dict = {}
Lnews_dict = {}

#Курсы крипты
btc_dict = {}
eth_dict = {}
ltc_dict = {}

#Новости крипты
CryptoNew_dict = {}

#Dp = диспетчер для комманд / Dispatcherfor command
dp = Dispatcher (bot)


#Сообщение в CMD о старте / Message about start in CMD
async def on_startup (_): #Задаем функцию / Setting the function
    print ("МУЗЫКА ПОШЛА") #Вывод сообщения / Output message


""" -----------------------------------------------------------------------------------------------------------------------------------"""


#MainMenu главное меню
niws = KeyboardButton('/news ✉️')
ixtr = KeyboardButton('/juk 🙂')
mainMenu = ReplyKeyboardMarkup (resize_keyboard=True).row(niws,ixtr)

#Back меню приколов
backMain = KeyboardButton('/backMain ❌')
backJuk = KeyboardButton('/backJuk ❌')
backKitty = KeyboardButton('/bacKitty ❌')

#ixtrMenu основное меню приколов
kits = KeyboardButton('/kitty 🦊')
joke = KeyboardButton('/joke 😂')
ixtrMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(kits,joke,backMain)

#KitsMenu меню с котами
sticker = KeyboardButton('/sticker 🎆') 
image = KeyboardButton('/image 🖼')
kitsMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(sticker,image,backJuk)

#StickerMenu меню стикеров котов
static = KeyboardButton('/tomcat 😼')
flexkit = KeyboardButton('/flexkitty 🐈')
stickerMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(static,flexkit,backKitty)

#Back меню новостей
backMain = KeyboardButton('/backMain ❌')
backNews = KeyboardButton('/backNews ❌')
backCyber = KeyboardButton('/backCyber ❌')
backCrypto = KeyboardButton('/backCryptos ❌')

#NewsMenu меню новостей базовое
cyber = KeyboardButton('/cybersports 💻')
crypto = KeyboardButton('/cryptos 📈')
world = KeyboardButton('/worldNews 🌏')
newsMenu = ReplyKeyboardMarkup (resize_keyboard=True).row(cyber,crypto,world,backMain)

#CyberMenu меню новостей киберспорта
dota = KeyboardButton('/Dota2 ⚔️')
cs = KeyboardButton('/CS 🔫')
lol = KeyboardButton('/LOL 🌈')
cyberMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(dota,cs,lol,backNews)

#CyberMenu меню новостей доты
newsDota = KeyboardButton('/Dnews ✉️')
the = KeyboardButton('/TI 🤸‍♀️')
DnewsMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(newsDota,the,backCyber)

#CyberMenu меню новостей кс
newsCS = KeyboardButton('/CSNews ✉️')
major = KeyboardButton('/Major 🤸‍♀️')
CnewsMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(newsCS,major,backCyber)

#CyberMenu меню новостей лола
newsL = KeyboardButton('/LNews ✉️')
worlds = KeyboardButton('/Worlds 🤸‍♀️')
LnewsMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(newsL,worlds,backCyber)

#Crypto меню для криптовалют
cryptonews = KeyboardButton('/cryptoNew ✉️')
btc = KeyboardButton('/BTC 🪬')
eth = KeyboardButton('/ETH 🔷')
ltc = KeyboardButton('/LTC 🧿')
cryptoMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(cryptonews,btc,eth,ltc,backNews)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Главные команды

#Комманда старта / Command start
@dp.message_handler (commands = ["start"]) #Задаем комманду / Setting the command
async def start  (message: types.Message): #Задаем функцию / Setting the function
    await bot.send_message( message.from_user.id, 'YEP начинаем',reply_markup = mainMenu) #Отправляем приветствие / Send hello
    await bot.send_message( message.from_user.id, 'Если хочешь узнать что я умею, пиши /help')
    await bot.send_sticker(message.chat.id,"CAACAgIAAxkBAAEFiWli9TsP9B1BLa8HrEqL51EtH4UQEAACnhYAArpIyUtcjAeK6Rs_SykE") #Отправляем стикер / Send sticker

@dp.message_handler (commands=["help"])
async def help (message: types.Message):
    await bot.send_message(message.chat.id, """Я специализируюсь на новостях киберспорта и критовалют, но также умею выдавать прикольчики
    Для новостей напиши /news
    Для прикольчиков напиши /juk
Также можно воспользоваться клавиатурой если писать впадлу.
У клавиатуры есть более быстрая навигация, чтобы ее узнать напиши /more""")

@dp.message_handler (commands=["more"])
async def more (message: types.Message):
    await bot.send_message(message.chat.id,"""Для быстрого получения контента можно прописать команду, а не прокликивать по клаве. 
Полный список комманд:
    /start (начать общение)
    /help (помощь)
    /more (больше информации)
    --------------------------
    /news (вывести меню новостей)
    /cybersports (вывести меню новостей киберспорта)
    /Dota2 (вывести меню новостей Dota 2)
    /Dnews (получить последние новости из мира Dota 2)
    /TI (получить информацию по прошедшему и следующему The International)
    /CS (вывести меню новостей Counter Strike Global Offensive)
    /Major (получить информацию по прошедшему и следующему Major)
    /CSnews (получить последние новости из мира CS GО)
    /LOL (вывести меню новостей League of Legend)
    /Lnews (получить последние новости из мира LOL'а)
    /Worlds (получить информацию по прошедшему и следующему Worlds)
    --------------------------
    /crytpos (вывести меню криптовалют)
    --------------------------
    /juk (вывести меню приколов)
    /joke (получить разрывную)
    /sticker (вывод меню стикеров с котами)
    /tomcat (получить статичный стикер с котом)
    /flexkitty (получить динамичный стикер с котом)
    /image (получить картинку кота)
    """)
    

""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Пока что не нужный кусок кода

#Вывод последней новости на данный момент / Output a last news at moment
@dp.message_handler(commands=["last"])
async def neks (message: types.Message):
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
        Dnews_dict [round_data] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("news_dict.json","w",encoding='utf-8') as file:
        json.dump(Dnews_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(Dnews_dict.items())[-1:]:
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Списки со стикерами и анекдотами

#Cписок id стикеров статичных котов / List id stickers static cats
stat = ["CAACAgIAAxkBAAEGReBjYN1bncaxE0k4O8yqWpHidwq-QQADFwACBud5SAZAQLkOAjyhKgQ", #CATS
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

#список разрывных
jokers = ["""Заходит однажды в бар улитка и говорит:
-Можно виски с колой?
- Простите, но мы не обслуживаем улиток.
И бармен вышвырнул ее за дверь.
Через неделю заходит опять эта улитка и спрашивает:
-Ну и нахуя ты это сделал!?""",
"""Бабушка перешла дорогу не на тот свет,
и попала на тот свет.""",
"""Как называют человека, который продал свою печень?
Обеспеченный.""",
"""Почему скелеты не пьют воду?
Потому-что вода это жидКость.""",
"""В семье скелетов родился сын. Назвали Костян."""]


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Главное меню

@dp.message_handler (commands=["news"])
async def neus (message: types.Message):
    await bot.send_message(message.from_user.id,"Займемся делом",reply_markup=newsMenu)

@dp.message_handler (commands=["juk"])
async def prikl(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери прикольчик",reply_markup=ixtrMenu)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Меню приколов

@dp.message_handler (commands=["joke"])
async def jk (message: types.Message):
    await bot.send_message(message.chat.id, choice(jokers))

@dp.message_handler (commands=["kitty"])
async def k (message: types.Message):
    await bot.send_message(message.from_user.id,"Выбери формат котика",reply_markup=kitsMenu)

@dp.message_handler (commands=["sticker"])
async def stic (message: types.Message):
    await bot.send_message(message.from_user.id,"Выбери формат стикера",reply_markup=stickerMenu)

@dp.message_handler (commands=["tomcat"])
async def sta (message: types.Message):
    await bot.send_sticker(message.chat.id,choice(stat))

@dp.message_handler (commands=["flexkitty"])
async def flx (message: types.Message):
    await bot.send_sticker(message.chat.id,choice(flex))


#Лист с фото
im = ["https://ru.pinterest.com/pin/113997434309824395/","https://commons.wikimedia.org/wiki/File:Cat%27s_Eyes.jpg?uselang=ru","https://commons.wikimedia.org/wiki/File:Black_Footed_Cat.jpg?uselang=ru"]

@dp.message_handler (commands=["image"])
async def img (message: types.Message):
    await bot.send_photo(message.chat.id,choice(im))


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Back'и для приколов

#Фразы для back'ов
literaly = ["Даем себаса","Оформляем себастьяна","Давим себастьяна","Базируемся в прошлое","Go back in time","Удаляем будущее","Шерудим себа","Обертас","Взадпятки","Критикуем пельмени","Шерудим ногами","ОП оп оп дал дал ушел"]

#Back'и меню приколов
@dp.message_handler (commands=["backMain"])
async def backmain (message: types.Message):
    await bot.send_message(message.from_user.id,choice(literaly),reply_markup=mainMenu)

@dp.message_handler (commands=["backJuk"])
async def backjuk (message: types.Message):
    await bot.send_message(message.from_user.id,choice(literaly),reply_markup=ixtrMenu)

@dp.message_handler (commands=["bacKitty"])
async def backitty (message: types.Message):
    await bot.send_message(message.from_user.id,choice(literaly),reply_markup=kitsMenu)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Cybersports

@dp.message_handler (commands=["cybersports"])
async def neuz (message: types.Message):
    await bot.send_message(message.from_user.id,"Киберспортс значится",reply_markup=cyberMenu)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#ДОТА

@dp.message_handler (commands=["dota2"])
async def neud (message: types.Message):
    await bot.send_message(message.from_user.id,"Дотку любишь побегать?",reply_markup=DnewsMenu)

#Парсер дота новостей с выводом
@dp.message_handler (commands=["Dnews"]) 
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
        Dnews_dict [round_data] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("Dnews_dict.json","w",encoding='utf-8') as file:
        json.dump(Dnews_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(Dnews_dict.items()):
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)

@dp.message_handler (commands=["TI"])
async def ti (message: types.Message):
    await bot.send_message(message.chat.id,"""
The International 2022
Дата проведения - c 15.10.2022 по 30.10.2022
Сумма призовых - $ 18 930 775
Место проведения - Сингапур
Участники (всего 6 регионов, 20 команд):

Китай:
Team Aster - 4
PSG.LGD - 5-6
Royal Never Give Up - 13-16 

Европа:
Thundra Esports - 1
Team Secret - 2
Team Liquid - 3
OG - 7-8
Glagiators - 9-12

СНГ:
Team Spirit - 13-16
BetBoom Team - 19-20

Южная Америка:
Thunder Awaken - 5-6
BeastCoast - 7-8
Hokori - 13-16

Малайзия:
BOOM Esports - 9-12
Fnatic - 13-16
Talon Esports - 17-18

Северная Америка:
Evil Geniuses 9-12
Entity - 9-12 
Soniqs - 17-18
TSM - 19-20

Победители - европейский коллектив Thundra Esports

На данный момент дата, место и формат проведения 
The International 2023 не известно""")


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#КСКА

@dp.message_handler (commands=["CS"])
async def neud (message: types.Message):
    await bot.send_message(message.from_user.id,"Кску любишь побегать?",reply_markup=CnewsMenu)

#Парсер кс новостей с выводом
@dp.message_handler (commands=["CSnews"]) 
async def news (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.cybersport.ru/tags/cs-go")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find_all (class_="rounded-block root_d51Rr with-hover no-padding no-margin")
    for round in rounded_block:
        round_title = round.find (class_="title_nSS03").text
        round_data = round.find (class_="pub_AKjdn").text
        round_link = round.find (class_="link_CocWY")
        round_url = f'https://www.cybersport.ru{round_link.get("href")}'
        CSnews_dict [round_data] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("CSnews_dict.json","w",encoding='utf-8') as file:
        json.dump(CSnews_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(CSnews_dict.items()):
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)

@dp.message_handler (commands=["major"])
async def neud (message: types.Message):
    await bot.send_message(message.from_user.id,"""
PGL Major Antwerp 2022
Дата проведения - с 08.05.2022 по 22.05.2022
Сумма призовых - $ 1 000 000
Место проведения - Антверпен, Бельгия
""")


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#LOL

@dp.message_handler (commands=["LOL"])
async def neud (message: types.Message):
    await bot.send_message(message.from_user.id,"Анимешник чишо?",reply_markup=LnewsMenu)

#Парсер лол новостей с выводом
@dp.message_handler (commands=["Lnews"]) 
async def news (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.cybersport.ru/tags/league-of-legends")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find_all (class_="rounded-block root_d51Rr with-hover no-padding no-margin")
    for round in rounded_block:
        round_title = round.find (class_="title_nSS03").text
        round_data = round.find (class_="pub_AKjdn").text
        round_link = round.find (class_="link_CocWY")
        round_url = f'https://www.cybersport.ru{round_link.get("href")}'
        Lnews_dict [round_data] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("Lnews_dict.json","w",encoding='utf-8') as file:
        json.dump(Lnews_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(Lnews_dict.items()):
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)

@dp.message_handler (commands=["Worlds"])
async def neud (message: types.Message):
    await bot.send_message(message.from_user.id,""" 321213
    """)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Crypto меню
@dp.message_handler (commands=["cryptos"])
async def cryptocurriens (message: types.Message):
    await bot.send_message(message.from_user.id,"Поговорим за деньги 😎", reply_markup=cryptoMenu)

@dp.message_handler (commands=["cryptoNew"])
async def cryptocurriens (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://cryptonews.net/ru/")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find_all (class_="col-xs-12 col-sm")
    for round in rounded_block:
        round_title = round.find(class_='desc col-xs')
        round_data = round.find (class_="datetime flex middle-xs")
        round_link = round.find (class_="desc col-xs")
        round_url = f'https://cryptonews.net/ru/{round_link.get("href")}'
        CryptoNew_dict [round_title] = {
            "time": round_data,
            "title": round_title,
            "url": round_url }

    with open ("CryptoNew_dict.json","w",encoding='utf-8') as file:
        json.dump(CryptoNew_dict, file, indent=4, ensure_ascii=False)

        for k,v in sorted(CryptoNew_dict.items()):
            news = f"<b>{v['time']}</b>\n"\
            f"{hlink(v['title'],v['url'])}"
            await message.answer(news)


""" -----------------------------------------------------------------------------------------------------------------------------------"""
#BTC

@dp.message_handler (commands=["BTC"])
async def bitocNews (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.vbr.ru/crypto/btc/")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find(class_="rates-best-table")

    #распаршиваем табл
    roundall = rounded_block.select("tr > td")

    #изменение за день
    isoRU = roundall[2] #isoRU
    isoDL = roundall[6] #isoDL
    isoEU = roundall[10] #isoEU

    #курс в рублях/долларах/евро
    roundRU = roundall[1] #valueRU
    roundDL = roundall[5] #valueDL
    roundEU = roundall[9] #valueDL

    #изменение за 14 дней
    is_14RU = roundall[3] #14RU
    is_14DL = roundall[7] #14DL
    is_14EU = roundall[11] #14EU

    #время последней котировка
    time = soup.find (class_="common-val nowrap") #time
    
    #словарь с информацией курса биткойна и его последних изменений
    btc_dict [url]= {

        "url":url,
        "title":"Кликни чтобы узнать больше:)",
        "time":"Котировка за "+time.text,

        "valueRU":"Курс в рублях: "+roundRU.text,
        "valueDL":"Курс в долларах: "+roundDL.text,
        "valueEU":"Курс в евро: "+roundEU.text,

        "isoRU":"Изменение за день: "+isoRU.text,
        "isoDL":"Изменение за день: "+isoDL.text,
        "isoEU":"Изменение за день: "+isoEU.text,

        "14RU":"Изменение за 14 дней: "+is_14RU.text,
        "14DL":"Изменение за 14 дней: "+is_14DL.text,
        "14EU":"Изменение за 14 дней: "+is_14EU.text
    }
    
    with open ("btc_dict.json","w",encoding='utf-8') as file:
        json.dump(btc_dict, file, indent=4, ensure_ascii=False)

    for key,value in btc_dict.items():
        nik = f"{hlink(value['title'],value['url'])}\n"
        news = f"<b>{value['time']}</b>\n"\
        f"{'₿ → ₱ 📊📊📊'}\n"\
        f"<b>{value['valueRU']}</b>\n"\
        f"<b>{value['isoRU']}</b>\n"\
        f"<b>{value['14RU']}</b>\n"\
        f"{'₿ → $ 📊📊📊'}\n"\
        f"<b>{value['valueDL']}</b>\n"\
        f"<b>{value['isoDL']}</b>\n"\
        f"<b>{value['14DL']}</b>\n"\
        f"{'₿ → € 📊📊📊'}\n"\
        f"<b>{value['valueEU']}</b>\n"\
        f"<b>{value['isoEU']}</b>\n"\
        f"<b>{value['14EU']}</b>"
        await message.answer(news)
        await message.answer(nik)
        
#ETH

@dp.message_handler (commands=["ETH"])
async def bitocNews (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.vbr.ru/crypto/eth/")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find(class_="rates-best-table")

    #распаршиваем табл
    roundall = rounded_block.select("tr > td")

    #изменение за день
    isoRU = roundall[2] #isoRU
    isoDL = roundall[6] #isoDL
    isoEU = roundall[10] #isoEU

    #курс в рублях/долларах/евро
    roundRU = roundall[1] #valueRU
    roundDL = roundall[5] #valueDL
    roundEU = roundall[9] #valueDL

    #изменение за 14 дней
    is_14RU = roundall[3] #14RU
    is_14DL = roundall[7] #14DL
    is_14EU = roundall[11] #14EU

    #время последней котировка
    time = soup.find (class_="common-val nowrap") #time
    
    #словарь с информацией курса биткойна и его последних изменений
    eth_dict [url]= {

        "url":url,
        "title":"Кликни чтобы узнать больше:)",
        "time":"Котировка за "+time.text,

        "valueRU":"Курс в рублях: "+roundRU.text,
        "valueDL":"Курс в долларах: "+roundDL.text,
        "valueEU":"Курс в евро: "+roundEU.text,

        "isoRU":"Изменение за день: "+isoRU.text,
        "isoDL":"Изменение за день: "+isoDL.text,
       "isoEU":"Изменение за день: "+isoEU.text,

        "14RU":"Изменение за 14 дней: "+is_14RU.text,
        "14DL":"Изменение за 14 дней: "+is_14DL.text,
        "14EU":"Изменение за 14 дней: "+is_14EU.text
    }
    
    with open ("eth_dict.json","w",encoding='utf-8') as file:
        json.dump(eth_dict, file, indent=4, ensure_ascii=False)

    for key,value in eth_dict.items():
        nik = f"{hlink(value['title'],value['url'])}\n"
        news = f"<b>{value['time']}</b>\n"\
        f"{'🔷 → ₱ 📊📊📊'}\n"\
        f"<u>{value['valueRU']}</u>\n"\
        f"<b>{value['isoRU']}</b>\n"\
        f"<b>{value['14RU']}</b>\n"\
        f"{'🔷 → $ 📊📊📊'}\n"\
        f"<u>{value['valueDL']}</u>\n"\
        f"<b>{value['isoDL']}</b>\n"\
        f"<b>{value['14DL']}</b>\n"\
        f"{'🔷 → € 📊📊📊'}\n"\
        f"<u>{value['valueEU']}</u>\n"\
        f"<b>{value['isoEU']}</b>\n"\
        f"<b>{value['14EU']}</b>"
        await message.answer(news)
        await message.answer(nik)

#LTC

@dp.message_handler (commands=["LTC"])
async def bitocNews (message: types.Message):
    header = {
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36"
    }
    url = ("https://www.vbr.ru/crypto/ltc/")
    r = requests.get (url=url)
    soup = BeautifulSoup (r.text, "lxml")
    rounded_block = soup.find(class_="rates-best-table")

    #распаршиваем табл
    roundall = rounded_block.select("tr > td")

    #изменение за день
    isoRU = roundall[2] #isoRU
    isoDL = roundall[6] #isoDL
    isoEU = roundall[10] #isoEU

    #курс в рублях/долларах/евро
    roundRU = roundall[1] #valueRU
    roundDL = roundall[5] #valueDL
    roundEU = roundall[9] #valueDL

    #изменение за 14 дней
    is_14RU = roundall[3] #14RU
    is_14DL = roundall[7] #14DL
    is_14EU = roundall[11] #14EU

    #время последней котировка
    time = soup.find (class_="common-val nowrap") #time
    
    #словарь с информацией курса биткойна и его последних изменений
    ltc_dict [url]= {

        "url":url,
        "title":"Кликни чтобы узнать больше:)",
        "time":"Котировка за "+time.text,

        "valueRU":"Курс в рублях: "+roundRU.text,
        "valueDL":"Курс в долларах: "+roundDL.text,
        "valueEU":"Курс в евро: "+roundEU.text,

        "isoRU":"Изменение за день: "+isoRU.text,
        "isoDL":"Изменение за день: "+isoDL.text,
       "isoEU":"Изменение за день: "+isoEU.text,

        "14RU":"Изменение за 14 дней: "+is_14RU.text,
        "14DL":"Изменение за 14 дней: "+is_14DL.text,
        "14EU":"Изменение за 14 дней: "+is_14EU.text
    }
    
    with open ("ltc_dict.json","w",encoding='utf-8') as file:
        json.dump(ltc_dict, file, indent=4, ensure_ascii=False)

    for key,value in ltc_dict.items():
        nik = f"{hlink(value['title'],value['url'])}\n"
        news = f"<b>{value['time']}</b>\n"\
        f"{'Ł → ₱ 📊📊📊'}\n"\
        f"<u>{value['valueRU']}</u>\n"\
        f"<b>{value['isoRU']}</b>\n"\
        f"<b>{value['14RU']}</b>\n"\
        f"{'Ł → $ 📊📊📊'}\n"\
        f"<u>{value['valueDL']}</u>\n"\
        f"<b>{value['isoDL']}</b>\n"\
        f"<b>{value['14DL']}</b>\n"\
        f"{'Ł → € 📊📊📊'}\n"\
        f"<u>{value['valueEU']}</u>\n"\
        f"<b>{value['isoEU']}</b>\n"\
        f"<b>{value['14EU']}</b>"
        await message.answer(news)
        await message.answer(nik)

""" -----------------------------------------------------------------------------------------------------------------------------------"""
#Back'и для cybersports

#Back для возврата в основное меню новостей
@dp.message_handler (commands=["backNews"])
async def backnew (message: types.Message):
    await bot.send_message(message.from_user.id,choice(literaly),reply_markup=newsMenu)

#Back'и меню новостей киберспорта
@dp.message_handler (commands=["backCyber"])
async def backcyb (message: types.Message):
    await bot.send_message(message.from_user.id,choice(literaly),reply_markup=cyberMenu)


""" -----------------------------------------------------------------------------------------------------------------------------------"""



#Запуск бота  
if __name__ == "__main__":
    executor.start_polling (dp, skip_updates=True, on_startup=on_startup)
