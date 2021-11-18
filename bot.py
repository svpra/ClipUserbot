#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import logging
import time
 
# Логирование
logging.basicConfig(filename="clip.log", filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

# Проверка библиотек
try:
    import wget
    from rich.console import Console
    from rich.text import Text
    from rich.progress import Progress
except:
    os.system("pip3 install rich")
    os.system("pip3 install wget")
    import wget
    from rich.console import Console
    from rich.text import Text
    from rich.progress import Progress

console = Console()

requirements = os.path.exists("requirements.txt")
if not requirements:
    wget.download("https://raw.githubusercontent.com/A9FM/filesUB/main/requirements.txt", "requirements.txt", bar=False)
else:
    os.remove("requirements.txt")
    wget.download("https://raw.githubusercontent.com/A9FM/filesUB/main/requirements.txt", "requirements.txt", bar=False)

with Progress() as progress:
    os.system("cls" if os.name == "nt" else "clear")
    requirements = progress.add_task("[red] Проверка зависимостей", total=10, refresh_per_second=1)
    filescheck = progress.add_task("[green] Проверка файлов", total=8, refresh_per_second=1)
    while not progress.finished:
        try:
            import telegraph
            progress.update(requirements, advance=1)
            import datetime
            progress.update(requirements, advance=1)
            import pyrogram
            progress.update(requirements, advance=1)
            import wikipedia
            progress.update(requirements, advance=1)
            import requests
            progress.update(requirements, advance=1)
            import gtts
            progress.update(requirements, advance=1)
            import youtube_dl
            progress.update(requirements, advance=1)
            import db0mb3r
            progress.update(requirements, advance=1)
            import configparser
            progress.update(requirements, advance=1)
            import wget
            progress.update(requirements, advance=1)
        except ModuleNotFoundError:
            progress.update(requirements, advance=1)
            os.system("pip install -q -r requirements.txt")
            os.system("cls" if os.name == "nt" else "clear")
            progress.update(requirements, advance=9)

        # Файлы
        import wget
        progress.update(filescheck, advance=1)
        configuration = os.path.exists("config.ini")
        if not configuration:
            wget.download("https://raw.githubusercontent.com/A9FM/filesUB/main/config.ini", "config.ini", bar=False)

        news = os.path.exists("news.txt")
        if not news:
            wget.download("https://raw.githubusercontent.com/A9FM/filesUB/main/news.txt", "news.txt", bar=False)
        else:
            os.remove("news.txt")
            wget.download("https://raw.githubusercontent.com/A9FM/filesUB/main/news.txt", "news.txt", bar=False)

        progress.update(filescheck, advance=1)
        stop = os.path.exists('stop.ogg')
        if not stop:
            wget.download('https://github.com/A9FM/filesUB/blob/main/stop.ogg?raw=true', "stop.ogg", bar=False)

        progress.update(filescheck, advance=1)
        update = os.path.exists("update.ogg")
        if not update:
            wget.download("https://github.com/A9FM/filesUB/blob/main/update.ogg?raw=true", "update.ogg", bar=False)

        progress.update(filescheck, advance=1)
        start = os.path.exists('start.ogg')
        if not start:
            wget.download('https://github.com/A9FM/filesUB/blob/main/start.ogg?raw=true', "start.ogg", bar=False)

        progress.update(filescheck, advance=1)
        reput = os.path.exists('rep.txt')
        if not reput:
            wget.download('https://raw.githubusercontent.com/A9FM/filesUB/main/rep.txt', "rep.txt", bar=False)

        progress.update(filescheck, advance=1)
        notes = os.path.exists('notes.txt')
        if not notes:
            wget.download('https://raw.githubusercontent.com/A9FM/filesUB/main/notes.txt', "notes.txt", bar=False)

        progress.update(filescheck, advance=1)
        floodw = os.path.exists('floodwait.txt')
        if not floodw:
            wget.download('https://raw.githubusercontent.com/A9FM/filesUB/main/floodwait.txt', "floodwait.txt", bar=False)

from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.handlers import MessageHandler
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from pyrogram.errors import FloodWait
from time import perf_counter, sleep, time
import random
import datetime
import asyncio
import sys
import wikipedia
import requests
import youtube_dl
import subprocess
import configparser
import shlex
from gtts import gTTS
from telegraph import Telegraph

version = "1.9.6 (Бета)"  # Версия юзербота

# Префиксы доп
config_path = os.path.join(sys.path[0], "config.ini")
config = configparser.ConfigParser()
config.read(config_path)


def get_prefix():
    prefix = config.get("prefix", "prefix")
    return prefix

try:
    prefix = get_prefix()
except:
    config.add_section("prefix")
    config.set("prefix", "prefix", ".")
    with open(config_path, "w") as config_file:
        config.write(config_file)
    prefix = "."

# Очистка терминала
os.system("cls" if os.name == "nt" else "clear")

# Логи + Вход
logi = "╭ Логи\n┃ "

# Перезагрузка, обновы
app = Client("my_account")

with app:
    app.join_chat("ArturDestroyerBot")  # Прошу, не убирайте эту строку
    app.unblock_user("ClipUSERBOT_LOGGERbot")
    app.unblock_user("ClipUSERBOT_NOTESbot")
    nowe = datetime.datetime.now()
    timnowe = nowe.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
    startlog = logi + timnowe + "\n╰ Юзербот был запущен"
    app.send_message("ClipUSERBOT_LOGGERbot", startlog)
    me = app.get_me()
    if len(sys.argv) == 4:
        try:
            restart_type = sys.argv[3]
            if restart_type == "1":
                app.send_audio(
                    sys.argv[1], "update.ogg", "✅ | Обновление <b>завершено!</b>"
                )
            else:
                app.send_audio(
                    sys.argv[1], "start.ogg", "✅ | Перезагрузка <b>завершена!</b>"
                )
        except:
            pass

with open("news.txt", "r+", encoding="utf-8") as f:
    news = str(f.read())
    os.system("cls" if os.name == "nt" else "clear")
    console.print(f"""[green]╔═╗╦  ╦╔═╗
║  ║  ║╠═╝
╚═╝╩═╝╩╩  [/green] [red]
╦ ╦╔═╗╔═╗╦═╗╔╗ ╔═╗╔╦╗
║ ║╚═╗║╣ ╠╦╝╠╩╗║ ║ ║ 
╚═╝╚═╝╚═╝╩╚═╚═╝╚═╝ ╩
Telegram Канал - @ArturDestroyerBot
Помощь - @Artur_destroyer
Версия {version} [/red]

[green][√] {me.first_name} - ({me.id}) Запущен[/green]

[blue]События:
{news} [/blue]
""")
    f.close()


# Помощь | Инфа про Юзербота
@app.on_message(filters.command("help", prefix) & filters.me)
async def helpp(client: Client, message: Message):
    try:
        logging.info("CLIP: Список комманд")

        await message.edit("🕐 Загрузка меню помощи. Пожалуйста подождите...")
        telegraph = Telegraph()
        telegraph.create_account(short_name='ClipUserbot')
        helpp = f"""<p align="center"><a href="https://github.com/A9FM/ClipUserbot"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/A9FM/ClipUserbot&title=Profile%20Views"></a></p>
<b><a href="https://t.me/ArturDestroyerBot">🤖 UserBot CLIP {version} 🤖</a></b><br>
<b><a href="https://9fm.github.io">👨 Создатель 💻</a></b><br>
<b><a href="https://www.donationalerts.com/r/a9fm">💰 Донат Создателю 💰</a></b><br>
<b><a href="https://github.com/A9FM/ClipUserbot#readme">🤔 Как установить? 🤔</a></b><br>
<a href="https://github.com/A9FM/filesUB/blob/main/README.md">© <b>Copyright ClipUSERBOT</b> ©</a><br>
<h3>Управление</h3>
<a href="#Основные">1.1 Основные</a><br>
<a href="#Мало-временни">1.2 Мало временни</a><br>
<a href="#Троллинг">1.3 Троллинг</a><br>
<a href="#Плюшки">1.4 Плюшки</a><br>
<a href="#Администрация">1.5 Администрирование</a><br>
<h3>Основные</h3>
⇛ <code>help</code> - Помощь | Информация | Проверка версии<br>
⇛ <code>ping</code> - Проверка Пинга Юзербота [Качество полключения]<br>
⇛ <code>restart</code> - Перезагрузка [Ошибка, Баг в Юзерботе]<br>
⇛ <code>update</code> - Обновить юзербота<br>
⇛ <code>beta</code> - Обновить юзербота на Бета версию<br>
⇛ <code>online</code> - Вечный онлайн (В сети/Стабильное подключение к интернету)<br>
⇛ <code>offline</code> - Отключение вечного онлайна<br>
⇛ <code>mnotes</code> [Ответ] [Название] - Сохранить сообщение <br>
⇛ <code>notes</code> [Число] - Вывести сообщение<br>
⇛ <code>mynotes</code> - Список всех notes<br>
⇛ <code>.sp</code> [Символ] - Смена префикса (знака в начале для комманд)<br>
<h3>Мало временни</h3>
⇛ <code>afk</code> [Причина] - Ввойти в АФК [Не в сети]<br>
⇛ <code>unafk</code> - Выйти из АФК<br>
⇛ <code>wiki</code> [Слово] - Поиск в Википедии<br>
⇛ <code>weather</code> [Город] - Погода<br>
<h3>Троллинг</h3>
⇛ <code>hack</code> - Взлом Пентагонна<br>
⇛ <code>jopa</code> - Взлом жопы<br>
⇛ <code>mum</code> - Поиск матери<br>
⇛ <code>drugs</code> - Принять 3aПрEщEHHblE BещECTBа<br>
⇛ <code>bomber</code> - Запуск Бомбера (Сайт)<br>
⇛ <code>sbomber</code> - Завершение роботы бомбера<br>
⇛ <code>q</code> [Ответ] - Сделать цитату (Стикер с текстом пользователя)<br>
⇛ <code>type</code> - Эффект Печати<br>
⇛ <code>hide</code> - Сообщения с Авто-удалением<br>
⇛ <code>progressbar</code> [Заголовок] - Прогресс бар (Загрузка)<br>
<h3>Плюшки</h3>
⇛ <code>sw</code> - Переключение расскладки [Если написали по типу ghbdtn]<br>
⇛ <code>short</code> [Ссылка] - сократитель ссылок<br>
⇛ <code>tagall</code> [Задержка в секундах] - Призыв всех участников<br>
⇛ <code>id</code> - Айди<br>
⇛ <code>info</code> - Информация<br>
⇛ <code>infofull</code> - Полная информация<br>
⇛ <code>qr</code> [Текст] - Создание QR-Кода с вашим текстом<br>
⇛ <code>time</code> - Текущее время<br>
⇛ <code>ladder</code> - текст лесенкой (п пр при прив привет)<br>
⇛ <code>webshot</code> [Ссылка] - Скриншот сайта<br>
⇛ <code>autoread</code> - Авто-чтение (Нет уведомлений с этого чата)<br>
⇛ <code>spam</code> [Кол-во смс] [Время между сообщениями в секундах] [Текст сообщения] - Спам<br>
⇛ <code>stspam</code> [Кол-во смс] [Время между сообщениями в секундах] [Айди стикера] - Спам стикерами<br>
⇛ <code>yt</code> [ссылка] - Скачивание и отправка видео (ютуб, тикток, лайк, инста)<br>
⇛ <code>myt</code> [ссылка] - Скачивание и отправа звука с видео (ютуб, тикток, лайк, инста)<br>
⇛ <code>spamban</code> - Проверка ограничений<br>
⇛ <code>voice</code> [Текст] - Текст в голосовое<br>
⇛ <code>text</code> [Ответ на голосовое] - Голосовое сообщение в текст<br>
⇛ <code>cl</code> [Текст] - Шифровка текста [Только пользователи CLIP]<br>
⇛ <code>eye</code> [Номер телефона] - Проверка номера в базе данных глаза бога<br>
⇛ <code>dem</code> [Текст] - Демотиватор<br>
⇛ <code>send</code> [Айди] - Написать человеку, зная его айди<br>
⇛ <code>link</code> [Ссылка] [Текст] - Ссылка в тексте<br>
⇛ <code>chance</code> [Текст] - Проверить шансы (например "Клип топ? Шансы 100%)<br>
⇛ Репутация<br>
<h3>Администрация</h3>
⇛ <code>ban</code> - Бан<br>
⇛ <code>unban</code> - Разбан<br>
⇛ <code>kick</code> - Кик<br>
⇛ <code>mute</code> - Мут<br>
⇛ <code>unmute</code> - Размут<br>
⇛ <code>aprefix</code> - Выдача звания админа<br>
⇛ <code>admin</code> - Выдача прав админа<br>
⇛ <code>unadmin</code> - Разжалование Админа<br>
⇛ <code>invite</code> (Юзейрнейм - @) - Пригласить в чат<br>
⇛ <code>kickall</code> - Удаление всех с чата<br>
⇛ <code>kickall hide</code> - Удаление всех (скрыто)<br>
⇛ <code>leave</code> - Выйти с чата<br>
⇛ <code>pin</code> - Закрепить<br>
⇛ <code>unpin</code> - Открепить<br>
<br>
Если нужна <b>помощь</b>, пиши <b><a href="https://t.me/a9_fm">@a9_fm</a></b><br>
"""
        response = telegraph.create_page(
            'Clip Userbot Помощь',
            html_content=f'{helpp}'
        )
        linkes = response['path']
        link = f'https://telegra.ph/{linkes}'
        await message.edit(f"""
<b>🚑 | Меню помощи</b>
<b>🔒 | Версия бота: {version}</b>

<b><a href="https://t.me/ClipUserbot">🙊 | Официальный чат поддержки пользователей CLIP.</a></b>
<b><a href={link}>❓ | Список всех команд </a></b>

<b><a href="https://a9fm.github.io">⛔️ | Ссылка на создателя CLIP</a></b>
<b><a href="https://t.me/dontcryplzs">❕ | Ссылка на помощника в разработке CLIP</a></b>

❤️ | Мы очень благодарны за использование нашего юзербота и желаем хорошего дня.
❤️ | Если вы нашли баги,можете написать создателю, помощнику, либо же в чат поддержки.
""", disable_web_page_preview=True)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")
        
# Доп код на рестарт
async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "bot.py",
                f"{message.chat.id}",
                f"{message.message_id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "bot.py",
                f"{message.chat.id}",
                f"{message.message_id}",
                f"{text}",
            ],
        )


# Рестарт
@app.on_message(filters.command("restart", prefix) & filters.me)
async def restartt(client: Client, message: Message):
    try:
        logging.info("CLIP: Перезагрузка юзербота")

        await message.delete()
        await app.send_audio(message.chat.id, "stop.ogg",
                             "🕦 | Идёт <b>перезагрузка</b>, пожалуйста подождите...")
        await restart(message, restart_type="restart")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Обновы
@app.on_message(filters.command("update", prefix) & filters.me)
async def updatte(client: Client, message: Message):
    try:
        logging.info("CLIP: Обновление юзербота")

        await message.edit("🕦 | Идёт <b>обновление</b>, пожалуйста подождите")
        os.remove("bot.py")
        wget.download("https://raw.githubusercontent.com/A9FM/ClipUserbot/main/bot.py", "bot.py")
        await restart(message, restart_type="update")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Обновы бета
@app.on_message(filters.command("beta", prefix) & filters.me)
async def beta(client: Client, message: Message):
    try:
        logging.info("CLIP: Обновление на Beta Версию")

        await message.edit("🕦 | Идёт <b>обновление на бета версию</b>, пожалуйста подождите...")
        os.remove("bot.py")
        wget.download("https://raw.githubusercontent.com/A9FM/ClipUserbot/beta/bot.py", "bot.py")
        await restart(message, restart_type="update")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Префикс
@app.on_message(filters.command("sp", ".") & filters.me)
async def pref(client: Client, message: Message):
    if len(message.command) > 1:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Префикс был сменён на [ " + message.command[1] + " ]"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        prefix = message.command[1]
        print(message.command)
        config.set("prefix", "prefix", prefix)
        with open(config_path, "w") as config_file:
            config.write(config_file)
        await message.edit(
            f"<b>✅ | Префикс [ <code>{prefix}</code> ] установлен!</b>\n⏳ | Пожалуйста, дождитесь окончания перезагрузки"
        )
        await restart(message, restart_type="restart")
    else:
        await message.edit("<b>⚠️ | Префикс не может быть пустым!</b>")


# Репутация
@app.on_message(filters.text & filters.incoming & filters.regex("^\-$") & filters.reply)
async def repMinus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:
            with open("rep.txt", "r+") as f:
                data1 = f.read()
                dat = int(data1)
                num = 1
                rep = dat - num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "❎ Осуждение оказано (-1)\n🌐 Текущая репутация: " + str(repo) + ""
                await message.reply_text(text)
            logging.info("CLIP: Понижение репутации")
    except:
        pass


@app.on_message(filters.text & filters.incoming & filters.regex("^\+$") & filters.reply)
async def repPlus(client: Client, message: Message):
    try:
        if message.reply_to_message.from_user.is_self:
            with open("rep.txt", "r+") as f:
                data = f.read()
                data = int(data)
                num = 1
                rep = data + num
                repo = str(rep)
                f.close()
            with open("rep.txt", "w+") as f:
                repo = str(rep)
                f.write(repo)
                f.close()
                text = "✅ Уважение оказано (+1)\n🌐 Текущая репутация: " + str(repo)
                await message.reply_text(text)
            logging.info("CLIP: Повышение репутации")
    except:
        pass

# Шансы
@app.on_message(filters.command("chance", prefix) & filters.me)
async def chance(client: Client, message: Message):
    try:
        logging.info("CLIP: Шанс")
        text = message.text.split(prefix + "chance ", maxsplit=1)[1]
        await message.edit(f"{text}\nВероятность {random.randint(1, 100)}%")

    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:
            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")
# Ссылка в тексте
@app.on_message(filters.command("link", prefix) & filters.me)
async def chance(client: Client, message: Message):
    try:
        logging.info("CLIP: Ссылка в тексте")

        link = message.command[1]
        text = " ".join(message.command[2:])
        await message.delete()
        await app.send_message(message.chat.id, f'<a href="{link}">{text}</a>', disable_web_page_preview=True)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:
            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error("CLIP: Нет заданых аргументов")
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")


# Прогресс бар
@app.on_message(filters.command("progressbar", prefix) & filters.me)
async def Progressbar(client: Client, message: Message):
    try:
        logging.info("CLIP: Прогресс бар")

        text = message.text.split(prefix + "progressbar ", maxsplit=1)[1]
        import time
        total = 100
        bar_length = 20
        for i in range(total + 1):
            percent = 100.0 * i / total
            time.sleep(0.0001)
            await message.edit(
                text + "\n[{:{}}] {:>3}%".format("█" * int(percent / (100.0 / bar_length)), bar_length, int(percent)))
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Написать пользотелю зная его айди
@app.on_message(filters.command("send", prefix) & filters.me)
async def sendtoid(client: Client, message: Message):
    try:
        logging.info("CLIP: Отправка текста SEND")

        await app.unblock_user(message.command[1])
        await message.edit(f"💬 | Отправлено сообщение пользователю {message.command[1]}")
        await app.send_message(message.command[1], "Привет!")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Айди
@app.on_message(filters.command("id", prefix) & filters.me)
async def id(client: Client, message: Message):
    try:
        logging.info("CLIP: Получение ID")

        if message.reply_to_message is None:
            await message.edit(f"👤 | Айди Чата: {message.chat.id}")
        else:
            id = f"👤 | Айди пользователя: {message.reply_to_message.from_user.id}\n📢 | Айди чата: {message.chat.id}"
            await message.edit(id)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Спам стикерами
@app.on_message(filters.command("stspam", prefix) & filters.me)
async def spam(client: Client, message: Message):
    try:
        if not message.text.split(prefix + "stspam", maxsplit=1)[1]:
            await message.edit("<i>Команда была введена неправильно</i>")

        count = message.command[1]
        slep = message.command[2]
        sticker = message.command[3]
        count = int(count)
        slep = int(slep)
        await message.delete()

        logging.info("CLIP: Спам стикерами")

        for _ in range(count):
            await app.send_sticker(message.chat.id, sticker)
            await asyncio.sleep(slep)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Бомбер
@app.on_message(filters.command("bomber", prefix) & filters.me)
async def b0mb3r(client: Client, message: Message):
    try:
        logging.info("CLIP: Запуск Бомбера")
        
        await message.edit("Запускаем бомбер")
        global bombe
        print("""
 _____                 _               
|  _  |               | |              
| |_) | ___  _ __ ___ | |__   ___ _ __ 
|  _ < / _ \| '_ ` _ \| '_ \ / _ \ '__|
| |_) | (_) | | | | | | |_) |  __/ |   
|____/ \___/|_| |_| |_|_.__/ \___|_|   
""")

        bombe = subprocess.Popen(["bomber"], stdout=subprocess.PIPE)
        await asyncio.sleep(5)
        await message.edit("Бомбер запущен!\nСсылка: 127.0.0.1:8080")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("sbomber", prefix) & filters.me)
async def sbomber(client: Client, message: Message):
    try:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Бомбер выключен"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        bombe.terminate()
        await message.edit("Бомбер завершил свою роботу...")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Демотиватор
@app.on_message(filters.command("dem", prefix) & filters.me)
async def demotivator(client: Client, message: Message):
    await message.edit("⏳ | Создаю демотиватор, это может занять некоторое время...")
    try:
        logging.info("CLIP: Создание демотиватора")

        if message.reply_to_message.photo:
            await app.unblock_user("memegeneration_bot")
            donwloads = await app.download_media(message.reply_to_message.photo.file_id)
            tuxt = message.text.split(prefix + "dem ", maxsplit=1)[1]
            text = "1. " + tuxt
            await app.send_photo(chat_id="memegeneration_bot", photo=donwloads, caption=text)
            await asyncio.sleep(4)
            iii = await app.get_history("memegeneration_bot")
            donwloads = await app.download_media(iii[0].photo.file_id)
            await app.send_photo(chat_id=message.chat.id, photo=donwloads)
            await message.delete()
            os.rmdir("/downloads/")
        else:
            await message.edit("❗️ | Сделайте реплай на изображение для создания демотиватора")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Время
@app.on_message(filters.command("time", prefix) & filters.me)
async def time(client: Client, message: Message):
    try:
        logging.info("CLIP: Вывод времени")

        timesnow = datetime.datetime.now().strftime('%d.%m.%Y\nВремя %H:%M:%S')
        await message.edit(f"Текущая дата: {timesnow}")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Читы репутация
@app.on_message(filters.command("rep", prefix) & filters.me)
async def repNakrutka(client: Client, message: Message):
    try:
        with open("rep.txt", "w+") as f:
            num = int(message.command[1])
            rep = num
            repo = str(rep)
            f.write(repo)
            f.close()
            text = "✅ | Вы успешно изменили свою репутацию.\n 🗓️ | Репутация " + str(repo) + ""
            await message.edit(text)

        logging.info("CLIP: Накручена репутация")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        await message.edit(
            f"❕ | Произошла ошибка!\n🗓️ | Репутация автоматически изменена на 0\n❓ | Команда для изменения репутации '.rep'")
        with open("rep.txt", "w+") as f:
            num = int(0)
            rep = num
            repo = str(rep)
            f.write(repo)
            f.close()


# Спам
@app.on_message(filters.command("spam", prefix) & filters.me)
async def spam(client: Client, message: Message):
    try:
        if not message.text.split(prefix + "spam", maxsplit=1)[1]:
            await message.edit("<i>Команда была введена неправильно</i>")
            return
        count = message.command[1]
        slep = message.command[2]
        text = " ".join(message.command[3:])
        count = int(count)
        slep = int(slep)
        await message.delete()

        logging.info("CLIP: Спам в чат")

        for _ in range(count):
            await app.send_message(message.chat.id, text)
            await asyncio.sleep(slep)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Скриншот сайта
@app.on_message(filters.command("webshot", prefix) & filters.me)
async def webshot(client: Client, message: Message):
    try:
        logging.info("CLIP: Скриншот сайта")

        try:
            if len(message.text.split()) < 2:
                await message.edit("<i>Нету аргументов.</i>")
                return
            user_link = message.command[1]
            await message.delete()
            full_link = (
                "https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{}".format(
                    user_link
                )
            )
            await app.send_photo(
                message.chat.id, full_link, caption=f"<b>Ссылка ⟶ {user_link}</b>"
            )

        except:
            if len(message.text.split()) < 2:
                await message.edit("<i>Нету аргументов.</i>")
                return
            user_link = message.command[1]
            await message.delete()
            full_link = (
                "https://webshot.deam.io/{}/?width=1920&height=1080?type=png".format(
                    user_link
                )
            )
            await app.send_photo(
                message.chat.id, full_link, caption=f"<b>Ссылка ⟶ {user_link}</b>"
            )

    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:
            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Видео с ютуб
@app.on_message(filters.command("yt", prefix) & filters.me)
async def yt(client: Client, message: Message):
    try:
        logging.info("CLIP: Скачивание видео")

        linked = message.command[1]
        await message.edit("⏳ | Скачивание видео. Это займёт некоторое время... (зависит от размера видео)")
        ydl_opts = {
            "outtmpl": "video.mp4",
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([linked])
        await message.edit("⏳ | Отправка видео. Это займёт некоторое время... (зависит от размера видео)")
        await app.send_video(
            chat_id=message.chat.id,
            video="video.mp4",
            caption="Оригинал: " + message.command[1],
        )
        await message.delete()
        os.remove("video.mp4")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("myt", prefix) & filters.me)
async def myt(client: Client, message: Message):
    try:
        logging.info("CLIP: Скачивание звука с видео")

        myth = "youtube-dl -f 140 " + message.command[1] + " -o music.m4a"
        await message.edit("⏳ | Скачивание аудиодорожки. Это займёт некоторое время (зависит от размера аудиодорожки)")
        os.system(myth)
        await message.edit("⏳ | Отправка аудиодорожки. Это займёт некоторое время (зависит от размера аудиодорожки)")
        await app.send_audio(
            chat_id=message.chat.id,
            audio="music.m4a",
            caption="❕ Данная аудиодорожка была взята с видео " + message.command[1],
        )
        await message.delete()
        os.remove("music.m4a")

    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Призыв всех
@app.on_message(filters.command("tagall", prefix) & filters.me)
async def tagall(client: Client, message: Message):
    try:
        logging.info("CLIP: Тегнуты все участники чата")

        slep = message.command[1]
        slep = int(slep)
        slepe = str(slep)
        args = " ! "
        if len(message.text.split()) >= 2:
            args = message.text.split(prefix + "tagall " + slepe, maxsplit=1)[1]
        await message.delete()
        chat_id = message.chat.id
        string = ""
        limit = 1
        members = app.iter_chat_members(chat_id)
        async for member in members:
            tag = member.user.username
            if limit <= 10:
                if tag != None:
                    string += f"<a href='https://t.me/{tag}'>᠋</a> "
                else:
                    string += f"<a href='tg://user?id={member.user.id}'>᠋</a> "
                limit += 1
            else:
                text = f"{args} |{string}"
                await app.send_message(chat_id, text, disable_web_page_preview=True)
                limit = 1
                string = ""
                await asyncio.sleep(slep)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Удалить смс
@app.on_message(filters.command("del", prefix) & filters.me)
async def delete_messages(client: Client, message: Message):
    try:
        if message.reply_to_message:
            try:
                logging.info("CLIP: Удаление сообщения")

                message_id = message.reply_to_message.message_id
                await app.delete_messages(message.chat.id, message_id)
                await message.delete()
            except FloodWait as e:
                mylastname = me.last_name
                await app.update_profile(last_name=f"{mylastname} | Флудвейт")
                await asyncio.sleep(e.x)
                await app.update_profile(last_name=f"{mylastname}")
    except:
    	pass

# Пурдж
@app.on_message(filters.command("purge", prefix) & filters.me)
async def purge(client: Client, message: Message):
    try:
        if message.reply_to_message:
            logging.info("CLIP: Удаление сообщений [purge]")

            r = message.reply_to_message.message_id
            m = message.message_id
            msgs = []
            await message.delete()
            v = m - r
            while r != m:
                msgs.append(int(r))
                r += 1
            await app.delete_messages(message.chat.id, msgs)
            r = message.reply_to_message.message_id
            msgs = []
            while r != m:
                msgs.append(int(r))
                r += 1
            await app.delete_messages(message.chat.id, msgs)
            await app.send_message(message.chat.id, f"<b>✅ | Удалено > {v} сообщений!</b>")
        else:
            await message.edit("<i>❗️ | Не могу найти реплай.</i>")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Команда type
@app.on_message(filters.command("type", prefix) & filters.me)
async def type(client: Client, message: Message):
    try:
        logging.info("CLIP: Команда type")

        orig_text = message.text.split(prefix + "type ", maxsplit=1)[1]
        text = orig_text
        tbp = ""
        typing_symbol = "▒"
        while tbp != orig_text:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            await asyncio.sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            await asyncio.sleep(0.10)

    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Лестница
@app.on_message(filters.command("ladder", prefix) & filters.me)
async def ladder(client: Client, message: Message):
    try:
        logging.info("CLIP: Текст лестницей")

        orig_text = message.text.split(prefix + "ladder ", maxsplit=1)[1]
        text = orig_text
        output = []
        for i in range(len(text) + 1):
            output.append(text[:i])
        ot = "\n".join(output)
        await message.edit(ot)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Quotes
@app.on_message(filters.command("q", prefix) & filters.me)
async def quotly(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Ответь на сообщение")
        return
    
    logging.info("CLIP: Цитата")

    await app.unblock_user("QuotLyBot")
    await message.edit("⌛️ | Создаю цитату. На это может потребоваться немного вашего драгоценного времени.")
    await message.reply_to_message.forward("QuotLyBot")
    await asyncio.sleep(5)
    iii = await app.get_history("QuotLyBot")
    await message.delete()
    await app.forward_messages(message.chat.id, "QuotLyBot", iii[0].message_id)


# Нотес
@app.on_message(filters.command("mnotes", prefix) & filters.me)
async def mnotes(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit("Ответь на сообщение")
            return
        
        logging.info("CLIP: Сохранение цитаты")

        await message.edit("Сохранение...")
        await app.unblock_user("ClipUSERBOT_NOTESbot")
        await message.reply_to_message.forward("ClipUSERBOT_NOTESbot")
        iii = await app.get_history("ClipUSERBOT_NOTESbot")

        with open("notes.txt", "r+") as f:
            notes = f.read()
            notesss = str(notes)
            f.close()
        with open("notes.txt", "w+") as f:
            name1 = message.text.split(prefix + "mnotes ", maxsplit=1)[1]
            notess = f"{notesss}\n{name1} - {prefix}notes {iii[0].message_id}"
            f.write(notess)
            f.close()

        await message.edit(
            f"✅ | Сообщение сохранено!\nДля вывода сообщения напишите <code>{prefix}notes {iii[0].message_id}</code>\nПолный список <code>.mynotes</code>")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("notes", prefix) & filters.me)
async def notes(client: Client, message: Message):
    try:
        logging.info("CLIP: Вывод цитаты")

        numbermess = int(message.command[1])
        await message.edit("Вывод сообщения...")
        await app.unblock_user("ClipUSERBOT_NOTESbot")
        await app.forward_messages(message.chat.id, "ClipUSERBOT_NOTESbot", numbermess)
        await message.delete()
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("mynotes", prefix) & filters.me)
async def notes(client: Client, message: Message):
    try:
        logging.info("CLIP: Вывод списка цитат")

        with open("notes.txt", "r+") as f:
            notesi = f.read()
            notesssssss = str(notesi)
            await message.edit(notesssssss)
            f.close()
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Ограничения
@app.on_message(filters.command("spamban", prefix) & filters.me)
async def spamban(client: Client, message: Message):
    try:
        logging.info("CLIP: Проверка на ограничения")

        await message.edit("⏳ | Проверяю твой аккаунт на наличие спам-бана. Это может занять некоторое время...")
        await app.unblock_user("spambot")
        await app.send_message("spambot", "/start")
        await asyncio.sleep(1)
        iii = await app.get_history("spambot")
        await message.delete()
        await app.forward_messages(message.chat.id, "spamBot", iii[0].message_id)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Удаление всех с группы (200 уч лимит)
@app.on_message(filters.command('kickall', prefix) & filters.me)
def kickall(client: Client, message: Message):
    try:
        logging.info("CLIP: Удаление всех участников")

        message.edit("‼️ | Начинаю удалять пользователей с чата. Это может занять некоторое время.)")
        num = 0
        for all in app.iter_chat_members(message.chat.id):
            try:
                num = + 1
                app.kick_chat_member(message.chat.id, all.user.id, 0)
            except:
                pass
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Удаление всех участников "
        app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")
        message.edit("Ошибка!\nПодробнее: @ClipUSERBOT_LOGGERbot")

@app.on_message(filters.command('kickall hide', prefix) & filters.me)
def kickall(client: Client, message: Message):
    try:
        logging.info("CLIP: Удаление всех участников [Скрыто]")

        message.delete()
        num = 0
        for all in app.iter_chat_members(message.chat.id):
            try:
                num = + 1
                app.kick_chat_member(message.chat.id, all.user.id, 0)
            except:
                pass
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Удаление всех участников (Скрытно)"
        app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")
        message.edit("Ошибка!\nПодробнее: @ClipUSERBOT_LOGGERbot")


# Инфа
@app.on_message(filters.command("infofull", prefix) & filters.me)
async def info(client: Client, message: Message):
    try:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Полная информация"
        await app.send_message("ClipUSERBOT_LOGGERbot", log)

        if message.reply_to_message:
            username = message.reply_to_message.from_user.username
            id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            user_link = message.reply_to_message.from_user.mention
            last_name = message.reply_to_message.from_user.last_name
            number = message.reply_to_message.from_user.phone_number
        else:
            username = message.from_user.username
            id = message.from_user.id
            first_name = message.from_user.first_name
            user_link = message.from_user.mention
            last_name = message.from_user.last_name
            number = "Скрыто [CLIP]"
        text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Фамилия: {last_name}
┃ Юзернейм: @{username}
┃ Номер телефона: {number}
╰ Ссылка: {user_link}
"""
        await message.edit(text, parse_mode="HTML")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("info", prefix) & filters.me)
async def info(client: Client, message: Message):
    try:
        logging.info("CLIP: Вывод информации")

        if message.reply_to_message:
            username = message.reply_to_message.from_user.username
            id = message.reply_to_message.from_user.id
            first_name = message.reply_to_message.from_user.first_name
            user_link = message.reply_to_message.from_user.mention
        else:
            username = message.from_user.username
            id = message.from_user.id
            first_name = message.from_user.first_name
            user_link = message.from_user.mention
        text = f"""
╭ <b>Информация</b>:
┃ Айди: <code>{id}</code>
┃ Имя: {first_name}
┃ Юзернейм: @{username}
╰ Ссылка: {user_link}"""
        await message.edit(text, parse_mode="HTML")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Пинг
@app.on_message(filters.command("ping", prefix) & filters.me)
async def ping(client: Client, message: Message):
    try:
        logging.info("CLIP: Пингование")

        start = perf_counter()
        await message.edit("Pong")
        end = perf_counter()

        start1 = perf_counter()
        await message.edit("ping")
        end1 = perf_counter()

        start2 = perf_counter()
        await message.edit("CLIP USERBOT Топ")
        end2 = perf_counter()

        pinges = ((end + end1 + end2) / 3) - ((start + start1 + start2) / 3)
        ping = pinges * 1000

        if 0 <= ping <= 199:
            await message.edit(
                f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟢 Стабильное"
            )
        if 199 <= ping <= 400:
            await message.edit(
                f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟠 Хорошее"
            )
        if 400 <= ping <= 600:
            await message.edit(
                f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n🔴 Не стабильное"
            )
        if 600 <= ping:
            await message.edit(
                f"<b>🏓 Понг\n📶</b> {round(ping)} мс\n⚠ Перепады связи"
            )
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Сократитель ссылок
@app.on_message(filters.command("short", prefix) & filters.me)
async def shorten_link_command(client: Client, message: Message):
    try:
        logging.info("CLIP: Сокращение ссылки")

        if message.reply_to_message:
            link = message.reply_to_message.text
        else:
            try:
                link = message.command[1]
            except IndexError:
                return await message.delete()
        api_key = "985cc63aaf6d4ac5f0d06bcb2d9c1d5b7a379"
        url = link
        api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
        data = requests.get(api_url).json()["url"]
        if data["status"] == 7:
            shortened_url = data["shortLink"]
            await message.edit(f"Сокращённая ссылка: {shortened_url}")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# QR-code
@app.on_message(filters.command("qr", prefix) & filters.me)
async def webshot(client: Client, message: Message):
    try:
        logging.info("CLIP: Скриншот сайта")

        if message.reply_to_message:
            text = message.reply_to_message.text
        elif len(message.text.split(maxsplit=1)) == 2:
            text = message.text.split(maxsplit=1)[1]
        text = text.replace(' ','%20')
        QRcode = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={text}"

        await message.delete()
        await app.send_photo(message.chat.id, QRcode)
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")


# Википедия
@app.on_message(filters.command("wiki", prefix) & filters.me)
async def wiki(client: Client, message: Message):
    try:
        logging.info("CLIP: Поиск информации в Википедии")

        lang = message.command[1]
        user_request = " ".join(message.command[2:])
        await message.edit("<b>Ищем инфу</b>")
        if user_request == "":
            wikipedia.set_lang("ru")
            user_request = " ".join(message.command[1:])
        try:
            if lang == "en":
                wikipedia.set_lang("en")

            result = wikipedia.summary(user_request)
            await message.edit(
                f"""<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>"""
            )
        except Exception as exc:
            await message.edit(
                f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>"""
            )
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Переключение раскладки
@app.on_message(filters.command("sw", prefix) & filters.me)
async def switch(client: Client, message: Message):
    try:
        logging.info("CLIP: Команда SW")

        text = " ".join(message.command[1:])
        ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
        en_keys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
        if text == "":
            if message.reply_to_message:
                reply_text = message.reply_to_message.text
                change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
                reply_text = str.translate(reply_text, change)
                await message.edit(reply_text)
            else:
                await message.edit("Текст отсутствует")
                await asyncio.sleep(3)
                await message.delete()
        else:
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            text = str.translate(text, change)
            await message.edit(text)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Шифровка сообщений
@app.on_message(filters.command("cl", prefix) & filters.me)
async def switch(client: Client, message: Message):
    try:
        logging.info("CLIP: Команда CL")

        text = " ".join(message.command[1:])
        ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
        en_keys = """異體字体♬♝♞♟γδεηθκλμνZXM∩SάằẫăǽẳßβЂ฿™đďÐðӘҾΣĤĦҤḦĥћҥḧŒœØỢ$śşŝšṧṩᵴﮐ§♌♍♎♏♐♑♒♓✵✶✷✸✹"""
        if text == "":
            if message.reply_to_message:
                reply_text = message.reply_to_message.text
                change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
                reply_text = str.translate(reply_text, change)
                await message.edit(reply_text)
            else:
                await message.edit("Текст отсутствует")
                await asyncio.sleep(3)
                await message.delete()
        else:
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            text = str.translate(text, change)
            await message.edit(text)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Погода
def get_pic(city):
    file_name = f"{city}.png"
    with open(file_name, "wb") as pic:
        response = requests.get("http://wttr.in/{citys}_2&lang=ru.png", stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name


# Погода
@app.on_message(filters.command("weather", prefix) & filters.me)
async def weather(client: Client, message: Message):
    try:
        logging.info("CLIP: Вывод погоды")

        city = message.command[1]
        await message.edit("🕑 Просматриваю погоду в вашей стране")
        r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=ru")
        await message.edit(f"🗺 Ваш город : {r.text}")
        await app.send_photo(
            chat_id=message.chat.id,
            photo=get_pic(city),
            reply_to_message_id=message.message_id,
        )
        os.remove(f"{city}.png")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Вечный онлайн
@app.on_message(filters.command("online", prefix) & filters.me)
async def online(client: Client, message: Message):
    try:
        online = True
        logging.info("CLIP: Включён вечный онлайн")

        await message.edit("✅ | Включён вечный онлайн")
        while online == True:
            await app.unblock_user("mafia_statistics_bot")
            await app.send_message("mafia_statistics_bot", "ок")
            iii = await app.get_history("mafia_statistics_bot")
            await app.delete_messages("mafia_statistics_bot", iii[0].message_id)
            await asyncio.sleep(60)
        else:
            await app.block_user("mafia_statistics_bot")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("offline", prefix) & filters.me)
async def offline(client: Client, message: Message):
    try:
        logging.info("CLIP: Отключение вечного онлайна")

        await message.edit("❎ | Вечный онлайн отключён")
        await restart(message, restart_type="restart")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Деанон - глаз бога
@app.on_message(filters.command("eye", prefix) & filters.me)
async def eye(client: Client, message: Message):
    try:
        logging.info("CLIP: Команда Eye | Деанон")

        await app.unblock_user("AnonymousEUEBot")
        number = message.command[1]
        await message.edit(
            f"⏳ | Проверяем аккаунт {number} на наличие деанонимизация. Это может занять некоторое время...")
        await app.send_message("AnonymousEUEBot", number)
        await asyncio.sleep(20)
        iii = await app.get_history("AnonymousEUEBot")
        await message.edit("Вот что удалось найти...")
        await app.forward_messages(message.chat.id, "AnonymousEUEBot", iii[0].message_id)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Поиск музыки
@app.on_message(filters.command("m", prefix) & filters.me)
async def send_music(client: Client, message: Message):
    try:
        logging.info("CLIP: Поиск музыки")

        cmd = message.command

        song_name = ""
        if len(cmd) > 1:
            song_name = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            song_name = (
                    message.reply_to_message.text or message.reply_to_message.caption
            )
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit("👀 | Не вижу название музыки,которое должен найти")
            await asyncio.sleep(2)
            await message.delete()
            return

        song_results = await app.get_inline_bot_results("deezermusicbot", song_name)

        try:
            # send to Saved Messages because hide_via doesn't work sometimes
            saved = await app.send_inline_bot_result(
                chat_id="me",
                query_id=song_results.query_id,
                result_id=song_results.results[0].id,
                hide_via=True,
            )

            # forward as a new message from Saved Messages
            saved = await app.get_messages("me", int(saved.updates[1].message.id))
            reply_to = (
                message.reply_to_message.message_id
                if message.reply_to_message
                else None
            )
            await app.send_audio(
                chat_id=message.chat.id,
                audio=str(saved.audio.file_id),
                reply_to_message_id=reply_to,
            )

            # delete the message from Saved Messages
            await app.delete_messages("me", saved.message_id)
        except TimeoutError:
            await message.edit("That didn't work out")
            await asyncio.sleep(2)
        await message.delete()
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Музыка"
        await app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")

        await message.edit("`⚠️ | Музыка не найдена\n❕ | Проверьте правильность названия трека.`")
        await asyncio.sleep(2)
        await message.delete()


# Текст в речь
@app.on_message(filters.command("voice", prefix) & filters.me)
async def voice(client: Client, message: Message):
    try:
        logging.info("CLIP: Текст в ГС")

        lang_code = os.environ.get("lang_code", "ru")
        cust_lang = None
        await message.delete()
        await app.send_chat_action(message.chat.id, "record_audio")
        text = message.text.split(None, 1)[1]
        tts = gTTS(text, lang=lang_code)
        tts.save("voice.mp3")
        if message.reply_to_message:
            await app.send_voice(
                message.chat.id,
                voice="voice.mp3",
                reply_to_message_id=message.reply_to_message.message_id,
            )
        else:
            await app.send_voice(message.chat.id, voice="voice.mp3")
        await app.send_chat_action(message.chat.id, action="cancel")
        os.remove("voice.mp3")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# AFK
async def afk_handler(client: Client, message: Message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start

        if message.from_user.is_bot is False:
            await message.reply_text(f"❕ Данный пользователь <b>AFK</b>.\n" f"<b>💬 Причина:</b> {reason}.\n" f"<b>⏳Длительность</b>: {afk_time}.")

    except NameError:
        pass


@app.on_message(filters.command("afk", prefix) & filters.me)
async def afk(client: Client, message: Message):
    try:
        logging.info("CLIP: Вход в АФК")

        global start, end, handler, reason
        start = datetime.datetime.now().replace(microsecond=0)
        handler = app.add_handler( 
            MessageHandler(afk_handler, (filters.private & ~filters.me | filters.group & filters.mentioned & ~filters.me)))
        if len(message.text.split()) >= 2:
            reason = message.text.split(" ", maxsplit=1)[1]
        else:
            reason = "Неизвестно"
        await message.edit(f"❕ Вход в <b>AFK режим</b>.\n<b>💬 Причина:</b> {reason}.\n")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# No AFK
@app.on_message(filters.command("unafk", prefix) & filters.me)
async def unafk(client: Client, message: Message):
    try:
        logging.info("CLIP: Выход с АФК")

        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = end - start
        await message.edit(
            f"❕ | Пользователь вышел с <b>AFK режима.</b> \n💬 Причина <b>AFK режима:</b> {reason}\n⏳ Длительность <b>AFK:</b> {afk_time}"
        )
        app.remove_handler(*handler)

    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Выход с АФК режима"
        await app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")
        await message.edit("<b>Я не был в АФК</b>")
        await asyncio.sleep(3)
        await message.delete()


# Автоудаление сообщений
@app.on_message(filters.command("hide", prefix) & filters.me)
async def hide(client: Client, message: Message):
    logging.info("CLIP: Скрытие сообщения")

    orig_text = message.text.split(prefix + "hide ", maxsplit=1)[1]
    await message.edit(orig_text)
    await asyncio.sleep(2)
    await message.delete()


# Авточтение
the_regex = r"^r\/([^\s\/])+"
i = filters.chat([])


@app.on_message(i)
async def auto_read(client: Client, message: Message):
    await app.read_history(message.chat.id)
    message.continue_propagation()


@app.on_message(filters.command("autoread", prefix) & filters.me)
async def add_to_auto_read(client: Client, message: Message):
    try:
        logging.info("CLIP: Авточтение сообщений (в чате)")

        if message.chat.id in i:
            i.remove(message.chat.id)
            await message.edit("❎ | Авточтение отключено")
        else:
            i.add(message.chat.id)
            await message.edit("✅ | Авточтение включено")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Админ комманды
def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


def get_args(message):
    try:
        message = message.text
    except AttributeError:
        pass
    if not message:
        return False
    message = message.split(maxsplit=1)
    if len(message) <= 1:
        return []
    message = message[1]
    try:
        split = shlex.split(message)
    except ValueError:
        return message
    return list(filter(lambda x: len(x) > 0, split))


async def CheckAdmin(message: Message):
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await app.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("⚠️ | Я не вижу права администратора. (Я вообще администратор?👀)")
        await asyncio.sleep(2)
        await message.delete()

    else:
        if SELF.status is not admin or SELF.can_restrict_members:
            return True
        else:
            await message.edit("⚠️ | Недостаточно прав администратора.")
            await asyncio.sleep(2)
            await message.delete()


@app.on_message(filters.command("leave", prefix) & filters.me)
async def leave(client: Client, message: Message):
    try:
        m = await message.edit("<code>Всем пока... [Пользователь вышел с чата]</code>")
        await asyncio.sleep(2)
        await app.leave_chat(chat_id=message.chat.id)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("unban", prefix) & filters.me)
async def unban(client: Client, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("👀 | Не вижу пользователя, которого требуется **разблокировать**")
                return
        try:
            get_user = await app.get_users(user)
            await app.unban_chat_member(chat_id=message.chat.id, user_id=get_user.id)
            await message.edit(f"✅ | Пользователь {get_user.first_name} был **разблокирован**")
        except:
            await message.edit("⚠️ | Я не могу **разблокировать.**")
    else:
        await message.edit("⚠️ | Права администратора **отсутствуют.**")


mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_stickers=False,
    can_send_animations=False,
    can_send_games=False,
    can_use_inline_bots=False,
    can_add_web_page_previews=False,
    can_send_polls=False,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@app.on_message(filters.command("mute", prefix) & filters.me)
async def mute_hammer(client: Client, message: Message):

    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("👀 | Не вижу пользователя, которого требуется **ограничить в отправке сообщений.**")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=mute_permission,
            )
            await message.edit(f"🤐 | Пользователь {get_user.first_name} был **ограничен в отправке сообщений**.")
        except:
            await message.edit("⚠️ | Я не могу **ограничить этого пользователя.**")
    else:
        await message.edit("⚠️ | Права администратора **отсутствуют.**")


unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@app.on_message(filters.command("unmute", prefix) & filters.me)
async def unmute(client: Client, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("👀 | Не вижу пользователя, которому требуется **снять ограничения.** ")
                return
        try:
            get_user = await app.get_users(user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
                permissions=unmute_permissions,
            )
            await message.edit(f"✅ | Пользователь {get_user.first_name} больше **не ограничен в отправке сообщений.**")
        except:
            await message.edit("⚠️ | Я не могу снять **ограничения с пользователя**")
    else:
        await message.edit("⚠️ | Права администратора **отсутствуют.**")


@app.on_message(filters.command("kick", prefix) & filters.me)
async def kick_user(client: Client, message: Message):
    if await CheckAdmin(message) is True:
        reply = message.reply_to_message
        if reply:
            user = reply.from_user["id"]
        else:
            user = get_arg(message)
            if not user:
                await message.edit("👀 | Я не вижу пользователя, которого требуется **исключить из чата.**")
                return
        try:
            get_user = await app.get_users(user)
            await app.kick_chat_member(
                chat_id=message.chat.id,
                user_id=get_user.id,
            )
            await message.edit(f"✅ | Пользователь {get_user.first_name} был **исключён из чата.**")
        except:
            await message.edit("⚠️ | Я не могу **исключить этого пользователя**")
    else:
        await message.edit("⚠️ | Права администратора **отсутствуют.**")


@app.on_message(filters.command("pin", prefix) & filters.me)
async def pin_message(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        admins = await app.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]

        if me.id in admin_ids:
            if message.reply_to_message:
                disable_notification = True

                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                await app.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("`✅ | Сообщение закреплено!`")
            else:
                await message.edit("`❕ | Не вижу сообщения,которое требуется закрепить!`")
        else:
            await message.edit("`⛔️ | Недостаточно прав`")
    else:
        await message.edit("`❗️ | Вы не администратор.`")
    await asyncio.sleep(3)
    await message.delete()


@app.on_message(filters.command("unpin", prefix) & filters.me)
async def pin(client: Client, message: Message):
    try:
        try:
            message_id = message.reply_to_message.message_id
            await app.unpin_chat_message(message.chat.id, message_id)
            await message.edit("✅ | Сообщение откреплено!")
        except:
            await message.edit("❕ | Не вижу сообщение,которое требуется открепить")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

@app.on_message(filters.command("aprefix", prefix) & filters.me)
async def promote(client, message: Message):
    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ.**")
        return
    title = "Admin"
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
        title = str(get_arg(message))
    else:
        args = get_args(message)
        if not args:
            await message.edit("**Я должен кого то повысить?**")
            return
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(message.chat.id, user, can_pin_messages=True)
        if title == "":
            title = "Админ"
        await message.edit(
            f"✅ | Пользователь {get_user.first_name} получил префикс администратора с текстом: **[{title}]**"
        )
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Выдан статус админа одному из участников"
        await app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
    if title:
        try:
            await app.set_administrator_title(message.chat.id, user, title)
        except:
            pass


@app.on_message(filters.command("admin", prefix) & filters.me)
async def promote(client, message: Message):
    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ.**")
        return
    title = "Admin"
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
        title = str(get_arg(message))
    else:
        args = get_args(message)
        if not args:
            await message.edit("**Я должен кого то повысить?**")
            return
        user = args[0]
        if len(args) > 1:
            title = " ".join(args[1:])
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=True,
            can_delete_messages=True,
            can_edit_messages=True,
            can_invite_users=True,
            can_promote_members=True,
            can_restrict_members=True,
            can_pin_messages=True,
            can_post_messages=True,
        )
        if title == "":
            title = "Админ"
        await message.edit(
            f"✅ | Пользователь {get_user.first_name} получил полного администратора с префиксом **[{title}]**"
        )
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Выдана админка одному из участников"
        await app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
    if title:
        try:
            await app.set_administrator_title(message.chat.id, user, title)
        except:
            pass


@app.on_message(filters.command("unadmin", prefix) & filters.me)
async def demote(client, message: Message):
    if await CheckAdmin(message) is False:
        await message.edit("**Я не админ**")
        return
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я могу разжаловать админа?**")
            return
    get_user = await app.get_users(user)
    try:
        await app.promote_chat_member(
            message.chat.id,
            user,
            is_anonymous=False,
            can_change_info=False,
            can_delete_messages=False,
            can_edit_messages=False,
            can_invite_users=False,
            can_promote_members=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_post_messages=False,
        )
        await message.edit(f"❎ | Пользователь {get_user.first_name} больше не **администратор!**")
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        now = datetime.datetime.now()
        timnow = now.strftime("Дата %d.%m.%Y • Время %H:%M:%S")
        log = logi + timnow + "\n╰ Разжалован админ"
        await app.send_message("ClipUSERBOT_LOGGERbot", f"{log}\n\nОШИБКА!\n{erryr}")
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")


@app.on_message(filters.command("invite", prefix) & filters.me)
async def invite(client: Client, message: Message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user["id"]
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Я должен кого то пригласить?**")
            return
    get_user = await app.get_users(user)
    logging.info("CLIP: Приглашение пользователя в чат")
    try:
        await app.add_chat_members(message.chat.id, get_user.id)
        await message.edit(
            f"✅ | Пользователь {get_user.first_name} **приглашён в этот чат!**"
        )
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefix) & filters.me)
async def hack(client: Client, message: Message):
    logging.info("CLIP: Команда Hack")

    try:
        perc = 0
        while perc < 100:
            text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        text = "✅ Пентагон успешно взломан!"
        await message.edit(str(text))
        await asyncio.sleep(3)
        perc = 0
        while perc < 100:
            text = "⬇️ Скачивание данных ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        await asyncio.sleep(1)
        text = "🐓Нашли файты что ты петух!"
        await message.edit(text)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Команда Взлома жопы
@app.on_message(filters.command("jopa", prefix) & filters.me)
async def jopa(client: Client, message: Message):
    logging.info("CLIP: Команда Jopa")

    try:
        perc = 0
        while perc < 100:
            text = "🍑 Взлом жопы в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        text = "✅ Жопа взломана"
        await message.edit(str(text))
        await asyncio.sleep(3)
        text = "🔍 Поиск Сливов ..."
        await message.edit(str(text))
        perc = 0
        await asyncio.sleep(3)
        while perc < 100:
            text = "⬇️ Скачивание сливов ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 4)
            await asyncio.sleep(0.15)
        text = "✅ Сливы были найдены"
        await message.edit(str(text))
        perc = 0
        await asyncio.sleep(5)
        while perc < 100:
            text = "⬆️ Продажа сливов барыге..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.15)
        text = "✅ Проданно"
        await message.edit(str(text))
        await asyncio.sleep(2)
        rand = random.randint(100, 5000)
        bal = rand
        text = "💸 Вы заработали " + str(bal) + " ₽"
        await message.edit(text)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")

            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

# Наркота
@app.on_message(filters.command("drugs", prefix) & filters.me)
async def drugs(client: Client, message: Message):
    logging.info("CLIP: Команда Drugs")
    try:
        perc = 0
        result = 0
        while perc < 100:
            text = "🍁Поиск запрещённых препаратов " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.1)
        text = "Найдено 3 кг шпекса🍪💨"
        await message.edit(str(text))
        await asyncio.sleep(3)
        text = "Оформляем вкид 🌿⚗️"
        await message.edit(str(text))
        await asyncio.sleep(5)
        drugsss = ['🔥😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты 😳🔥',
                   '🥴Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид🥴',
                   '😖Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз😖',
                   '😌Вы оформили вкид, Вам понравилось)😌']
        drug = random.choice(drugsss)
        await message.edit(drug)
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")
    
# Оскорбление мамки
@app.on_message(filters.command("mum", prefix) & filters.me)
async def mum(client: Client, message: Message):
    logging.info("CLIP: Команда Mum")

    try:
        text = "🔍 Поиск твоей мамки начался..."
        await message.edit(str(text))
        await asyncio.sleep(3.0)
        perc = 0
        while perc < 100:
            text = "🔍 Ищем твою мамашу на Авито... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            await asyncio.sleep(0.75)
        text = "❌ Мамаша не найденна"
        await message.edit(str(text))
        await asyncio.sleep(3.0)
        perc = 0
        while perc < 100:
            text = "🔍 Поиск твоей мамаши на свалке... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.75)
        text = "❌ Мамаша не найденна"
        await message.edit(str(text))

        perc = 0
        while perc < 100:
            text = "🔍 Поиск твоей мамки в канаве... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            await asyncio.sleep(0.75)
        text = "✅ Мамка найдена... Она в канаве"
        await message.edit(str(text))
    except FloodWait as e:
        with open("floodwait.txt", "w+") as f:

            if me.last_name == None:
                f.write("᠋")
            else:
                f.write(me.last_name)
            f.close()
        with open("floodwait.txt", "r+") as f:
            opisanie = f.read()
            await app.update_profile(last_name=f"{opisanie} | Флудвейт")
            await asyncio.sleep(e.x)
            await app.update_profile(last_name=f"{opisanie}")
            f.close()
    except Exception as erryr:
        logging.error(erryr)
        await message.edit(f"⚠️ | Что-то пошло не так...\n💬 | Просмотреть ошибку можно здесь: @ClipUSERBOT_LOGGERbot")
        await app.send_document("ClipUSERBOT_LOGGERbot", "clip.log")

app.run()