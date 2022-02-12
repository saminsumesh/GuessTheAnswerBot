from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import GUESS_COUNT, MAX_GUESSES, SECRET_WORD, API_ID, API_HASH, BOT_TOKEN



Client = Client(
  "Guess Bot",
  API_ID,
  API_HASH,
  bot_token=BOT_TOKEN
)

guess = ""
out_of_guesses = False

@Client.on_message(filters.command("start"))
async def start(bot, m:Message):
  await m.reply_text(START_TXT.format(m.from_user.mention),
  reply_markup=InlineKeyboardMarkup(
    [[
      InlineKeyboardButton("Start Guessing", callback_data="game")
    ]]
  ))

@Client.on_callback_query("game")
async def game(bot, m:Message):
  while guess != SECRET_WORD and not(out_of_guesses):
    if GUESS_COUNT < MAX_GUESSES:
      guess = await m.reply_text(f"Enter your guesses : ")
      GUESS_COUNT += 1
    else:
      out_of_guesses = True
      
  if out_of_guesses:
    await m.reply_text("Sorry, " + (m.from_user.mention) + " You're out of guesses, YOU LOSE")
  else:
    await m.reply_text("Hurray " + (m.from_user.mention) + " You've won the guess")


Client.run()
