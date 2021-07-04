from pyrogram import Client, filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions, Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from time import sleep, perf_counter
from pyrogram.handlers import MessageHandler
from covid import Covid
import time, random, datetime, asyncio, sys, wikipedia, requests, os

# Для логов уберите знак "#"  ниже
import logging

print("""  ____ _     ___ _____
 / ___| |   |_ _|  _  |
| |   | |    | || |_) |
| |___| |___ | ||  ___|
 \____|_____|___|_|
    _       ___            _____   __  __
   / \     / _ \          |  ___| |  \/  |
  / _ \   | (_) |  _____  | |_    | |\/| |
 / ___ \   \__, | |_____| |  _|   | |  | |
/_/   \_\    /_/          |_|     |_|  |_|

Telegram Канал - @ArturDestroyerBot
Помощь - @ArturDestroyer

Логи:""")

app = Client("my_account")
# Вход в группу [Обновления]
with app:
    app.join_chat('ArturDestroyerBot') # Прошу, не убирайте эту строку
# Информация про бота
@app.on_message(filters.command("info" , prefixes=".") & filters.me)
def hack(_, msg):
    msg.edit("UserBot [CLIP]\nVersion 1.5.4\nCreator @artur_destroyer")

# Помощь
@app.on_message(filters.command("help" , prefixes=".") & filters.me)
def hack(_, msg):
    msg.edit("""UserBot CLIP [ @ArturDestroyerBot ]
КОММАНДЫ

Основные:
.help - Помощь
.info - Информация | Проверка Версии юзербота
.ping - Проверка Пинга бота [Качество полключения]

Мало временни:
.afk [Причина] - Ввойти в АФК [Не в сети]
.unafk - Выйти из АФК
.wiki [Слово] - Поиск в Википедии
.autoread - АвтоПросмотр [Не получать новые уведомления с чата]
.covid [Страна] - Статистика заражения вирусом covid-19 [Коронавирус]
.weather [Город] - Погода

Процент загрузки:
.hack - Взлом Пентагонна
.jopa - Взлом жопы
.mum - Поиск матери
.drugs - Принять 3aПрEщEHHblE BещECTBа

Спам:
.spam - Спам текстом и Смайлами
.spamt - Спам Текстом
.spams - Спам стикерами
.stop - Стоп спам

Плюшки:
.type - Эффект Печати
.hide - Сообщения с Авто-удалением
.sw - Переключение расскладки [Если написали по типу ghbdtn]

Если нужна помощь, пиши @artur_destroyer

Видео Гайд
https://youtu.be/iybTpYnRY2Y""")
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            msg.edit(tbp)
            sleep(0.10)
        except FloodWait as e:
            sleep(e.x)
# Пинг
@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client: Client, message: Message):
    start = perf_counter()
    await message.edit('Pong')
    end = perf_counter()
    ping = end - start
    await message.edit(f'<b>🏓 Понг \n📶</b><code> {round(ping, 3)}МС</code>')

# Covid
@app.on_message(filters.command("covid", prefixes=".") & filters.me)
async def covid_local(client: Client, message: Message):
    region = ' '.join(message.command[1:])
    await message.edit('<code>Загрузка...</code>')
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit("<b>=======🦠 COVID-19 STATUS 🦠=======</b>\n" +
                           f"<b>Регион [Страна]</b>: <code>{local_status['country']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>🤧 Новые заражения</b>: <code>{local_status['new_cases']}</code>\n" +
                           f"<b>😷 Новые смерти</b>: <code>{local_status['new_deaths']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>😷 Подтверждённые</b>: <code>{local_status['confirmed']}</code>\n" +
                           f"<b>❗️ Активные [Заражённые]:</b> <code>{local_status['active']}</code>\n" +
                           f"<b>⚠️ Критически</b>: <code>{local_status['critical']}</code>\n" +
                           f"<b>💀 Смертей</b>: <code>{local_status['deaths']}</code>\n" +
                           f"<b>🚑 Спасенно [Вылеченно]</b>: <code>{local_status['recovered']}</code>\n")
    except ValueError:
        await message.edit(f'<code>There is no region called "{region}"</code>')


# Википедия
@app.on_message(filters.command("wiki", prefixes=".") & filters.me)
async def wiki(client: Client, message: Message):
    lang = message.command[1]
    user_request = ' '.join(message.command[2:])
    if user_request == '':
        wikipedia.set_lang("ru")
        user_request = ' '.join(message.command[1:])
    try:
        if lang == 'en':
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f'''<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>''')
    except Exception as exc:
        await message.edit(f'''<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>''')
# Переклюяение раскладки
@app.on_message(filters.command("sw", prefixes=".") & filters.me)
async def switch(client: Client, message: Message):
    text = ' '.join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    if text == '':
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            message.edit('No text for switch')
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)

# Погода
def get_pic(city):
    file_name = f'{city}.png'
    with open(file_name, 'wb') as pic:
        response = requests.get('http://wttr.in/{citys}_2&lang=rus.png', stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

@app.on_message(filters.command("weather", prefixes=".") & filters.me)
async def weather(client: Client, message: Message):
    city = message.command[1]
    await message.edit("```Processing the request...```")
    r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=en")
    await message.edit(f"```City: {r.text}```")
    await client.send_document(chat_id=message.chat.id, document=get_pic(city), reply_to_message_id=message.message_id)
    os.remove(f'{city}.png')


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
    while(perc < 100):
        try:
            text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("✅ Пентагон успешно взломан!")
    sleep(3)
    perc = 0
    while(perc < 100):
        try:
            text = "⬇️ Скачивание данных ..." + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 5)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("🐓Нашли файты что ты петух!")

# Команда Взлома жопы
@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
    while(perc < 100):
        try:
            text = "🍑 Взлом жопы в процессе ..." + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("✅ Жопа взломана")
    sleep(3)
    msg.edit("🔍 Поиск Сливов ...")
    perc = 0
    sleep(3)
    while(perc < 100):
        try:
            text = "⬇️ Скачивание сливов ..." + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 4)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("✅ Сливы были найденны")
    perc = 0
    sleep(5)
    while(perc < 100):
        try:
            text = "⬆️ Продажа сливов барыге..." + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 5)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)

    msg.edit("✅ Проданно")
    sleep(3)
    perc = 0

    while(perc < 100):
        try:
            text = "⬇️ Выводим средства..." + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 20)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    perc = 0
    perc += random.randint(100, 5000)
    text = "💸 Вы заработали " + str(perc) + " Рублей"
    msg.edit(text)

# Наркотики - злооооооооо, комманда .drugs
# Код - @frontcoders
@app.on_message(filters.command("drugs", prefixes=".") & filters.me)
def drugs(_, msg):
    perc = 0
    result = 0
    while(perc < 100):
        try:
            text = "🍁Поиск запрещённых препаратов " + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("Найдено 3 кг шпекса🍪💨")
    sleep(3)
    msg.edit("Оформляем вкид 🌿⚗️")
    sleep(5)
    result += random.randint(1, 4)

    if result == 1:
        msg.edit("😳Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты😳🔥")
    if result == 2:
        msg.edit("Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте ещё раз оформить вкид")
    if result == 3:
        msg.edit("Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз")
    if result == 4:
        msg.edit("Вы оформили вкид, Вам понравилось)")

# Оскорбление мамки
@app.on_message(filters.command("mum" , prefixes=".") & filters.me)
def hack(_, msg):
    msg.edit("🔍 Поиск твоей мамки начался...")
    sleep(3.0)
    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Ищем твою мамку на свалке... " + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 3)
            sleep(0.25)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("❌ Мать не найденна...")
    sleep(3.0)
    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамки в канаве... " + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 5)
            sleep(0.25)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("✅ Мамка найдена... Она в канаве")

# СПАМ
@app.on_message (filters.command("spamt" , prefixes=".") & filters.me)
async def hello (client, message):
    global spam
    spam = 0
    await message.reply_text("Стартуем :3")
    while(spam < 1000000):
        try:
            await message.reply_text("Спам!!!")
            spam += 1
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("spams", prefixes="."))
async def hello (client, message):
    global spam
    spam = 0
    await message.reply_text("Spam started!")
    while(spam < 1000000):
        try:
            await message.reply_text("😡")
            spam += 1
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("spam", prefixes="."))
async def hello (client, message):
    global spam
    spam = 0
    await message.reply_text("Spam started!")
    while(spam < 1000000):
        try:
            await message.reply_text("😡")
            await message.reply_text("Spam")
            spam += 1
        except FloodWait as e:
            sleep(e.x)

# Стоп спам
@app.on_message (filters.command("stop" , prefixes=".") & filters.me)
async def hello (client, message):
        global spam
        spam = 0
        await message.reply_text("Стоп спам...")
        spam += 1000000

# AFK
async def afk_handler(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        if message.from_user.is_bot is False:
            await message.reply_text(f"<b>Я АФК уже {afk_time}</b>\n"
                                     f"<b>Причина:</b> <i>{reason}</i>")
    except NameError:
        pass

@app.on_message (filters.command("afk" , prefixes=".") & filters.me)
async def afk(client, message):
    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(MessageHandler(afk_handler, (filters.private & ~filters.me)))
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "Неизвестно"
    await message.edit(f"Теперь я АФК</b>\n"
                       f"<b>Причина:</b> <i>{reason}</i>")

# No AFK
@app.on_message (filters.command("unafk" , prefixes=".") & filters.me)
async def unafk(client, message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        await message.edit(f"<b>Я теперь не АФК.\nБыл в афк {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>Я не был в АФК</b>")
        await asyncio.sleep(3)
        await message.delete()

# Автоудаление сообщений
@app.on_message(filters.command("hide", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".hide ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.02)
            tbp = tbp + text[0]
            text = text[1:]
            msg.edit(tbp)
            sleep(0.02)
        except FloodWait as e:
            sleep(e.x)
    sleep(3)
    msg.edit("Deleted!")

@app.on_message(filters.command("a9fm", prefixes="."))
def type(_, msg):
    perc = 0
    while(perc < 25):
        try:
            msg.edit("Artur Destroyer")
            sleep(1)
            msg.edit("Hacker")
            sleep(1)
            msg.edit("A9FM")
            sleep(1)
            msg.edit("Anonimous")
            sleep(1)
            msg.edit("Python developer")
            sleep(1)
            msg.edit("Destroyer")
            sleep(1)
            msg.edit("Rox Tigers Top")
            sleep(1)
            msg.edit("Create UserBot_Clip")
            sleep(1)
            msg.edit("Vzlom Jopi")
            sleep(1)
            msg.edit("Hack You")
            sleep(1)
            msg.edit("Pyrogram top!")
            sleep(1)
            msg.edit("C++ govno")
            sleep(1)
            msg.edit("PhP huita")
            sleep(1)
            msg.edit("JS for louser")
            sleep(1)
            msg.edit("I am use CLIP_UserBot")
            sleep(1)
            perc += 1
        except FloodWait as e:
            sleep(e.x)
    msg.edit("@artur_destroyer")

app.run()
