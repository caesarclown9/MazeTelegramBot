import datetime
import json
import logging
import sys, os, random

import telebot
import requests
from decouple import config
from PIL import Image

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

bot = telebot.TeleBot(config("TOKEN"))
TOKEN = config("TOKEN")
CHAT_ID = config('KRIS_ID')

URL = f"https://api.telegram.org/bot{TOKEN}/"

def run(event, context):
    rand_pic = random.choice(os.listdir('mazebot'))
    PHOTO = Image.open(f'mazebot/{rand_pic}')
    bot.send_photo(chat_id=CHAT_ID, photo=PHOTO)


def say_meow(text, chat_id):
    meow = 'Мяу'
    url = URL + f'sendmessage?meow={meow}&chat_id={chat_id}'
    requests.get(url)

def lambda_handler(event, context):
    message = json.loads(event['body'])
    chat_id = message['message']['chat']['id']
    reply = message['message']['text']
    say_meow(reply, chat_id)
    return {'statusCode': 200}