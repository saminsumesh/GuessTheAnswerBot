import os
from os import environ

API_ID = int(environ.get("API_ID"))

API_HASH = environ.get("API_HASH")

BOT_TOKEN = environ.get("BOT_TOKEN")

START_TXT = """Hey {}, Iam a Guess Game Bot 

Hope You Enjoyed The Bot
"""

GUESS_COUNT = int(environ.get("GUESS_COUNT", ""))

MAX_GUESSES = int(environ.get("MAX_GUESSES", ""))

SECRET_WORD = envrion.get("Any word that you want your users to guess")
