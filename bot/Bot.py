import telebot
from logging import INFO
from logging import DEBUG

telebot.logger.setLevel(INFO) # Oppure DEBUG

API_TOKEN = "INSERT_TOKEN_HERE"

if API_TOKEN == "":
	exit("Inserire un token!")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.from_user.id,
		f"Ciao {message.from_user.first_name}!")

@bot.message_handler(func=lambda message: message.text)
def echo(message):
	bot.send_message(message.from_user.id,message.text)
	print(message.text)

try:
	bot.polling()
except:
	print("Hai staccato la connessione, vero?")
