import telebot
import os

# यहाँ अपने टेलीग्राम बॉट का असली टोकन डाल देना (कोट्स के अंदर)
TOKEN =9273529122:AAGtGX3UtZxviJxsYLDmXy UpG4a14MRRd4w
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "नमस्ते! मेरा Free Fire Like Bot चालू हो गया है! 🔥")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "नमस्ते! मैंने तेरा मैसेज देख लिया है!")

# Render के लिए जरूरी वेब सर्वर (ताकि बॉट 24/7 चालू रहे)
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive 24/7!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    bot.infinity_polling()
  
