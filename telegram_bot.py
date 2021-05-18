# -*- coding: utf-8 -*-
"""
Created on Tue May 18 07:10:25 2021


 KRILL-LOTIN TELEGGRAM BOT
 
@author: Islomiddin
"""

from transliterate import to_cyrillic,to_latin
import telebot

bot = telebot.TeleBot("1860676108:AAG-A3OiMl2nxKGJRYkLB3dXFjVZSO_Ie08", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob='Assalomu alaykum,Xush kelibsiz! '
    javob+='\nMatn kiriting'
    javob+='\n(bot admini Islomiddin Anvarjonov)'
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
   #javob=lambda msg:to_cyrillic(msg) if  msg.isascii() esle to_latin(msg)
    if msg.isascii():
        javob=to_cyrillic(msg)
        
    else:
        javob=to_latin(msg)
        
    bot.reply_to(message, javob)

bot.polling()
