import os
from os import environ

API_ID = int(os.environ.get("API_ID")

API_HASH = os.environ.get("API_HASH")

BOT_TOKEN = os.environ.get("BOT_TOKEN")

START_TXT = """Hey {}, Iam a Guess Game Bot 

Hope You Enjoyed The Bot
"""

GUESS_COUNT = int(os.environ.get("GUESS_COUNT", "")

MAX_GUESSES = int(os.environ.get("MAX_GUESSES", "")

SECRET_WORD = os.envrion.get("Any word that you want your users to guess")
