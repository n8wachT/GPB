# -*- coding: utf-8 -*-
import telebot
from Utils import build_plugins, init_groups
#from SDBApi import SDBApi
#server = SDBApi()
admins = [59802458]
disabled_files = ['Store.py']
disabled_plugins = []
strict_errors = False
command_char = '/'
#PASTE YOUR TOKEN HERE 
token = ''
if(token == ''):
    token = raw_input('No token detected, please paste or type here your token:\n> ')
print('token = ['+token+']')
groups = init_groups()
bot = telebot.TeleBot(token)
me = bot.get_me()
username = me.username
nickname = me.first_name
print('Bot username: [@' + username + ']')
print('Bot nickname: [' + nickname + ']')
print('Command char: [' + command_char + ']')

plugins = build_plugins(bot, 'plugins', disabled_files)
ignored_chats = []
