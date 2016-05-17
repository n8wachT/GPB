# -*- coding: utf-8 -*-
import telebot
from Utils import build_plugins, init_groups
#comment the following line to use default timeout.
telebot.apihelper.CONNECT_TIMEOUT = 9999
#Put your id here to use admin-only plugins.
admins = [59802458]
#List of plugins that will not be loaded. Ex. ['Echo.py', 'Who.py']
disabled_files = ['Chat.py', 'Qr.py', 'Stickers.py']
#Plugins that will be disabled at runtime if they throws exceptions.
#Don't edit.
disabled_plugins = []
#Set to True if you want to disable permanently a plugin that throws
#exceptions.
strict_errors = False
#Starting character for commands.
command_char = '/'
#PASTE YOUR TOKEN HERE 
token = ''
if(token == ''):
    token = raw_input('No token detected, please paste or type here your token:\n> ')
print('token = ['+token+']')
##INITIALIZATION SECTION.
groups = init_groups()
bot = telebot.TeleBot(token)
me = bot.get_me()
ignore_old = True
username = me.username
nickname = me.first_name
print('Bot username: [@' + username + ']')
print('Bot nickname: [' + nickname + ']')
print('Command char: [' + command_char + ']')

plugins = build_plugins(bot, 'plugins', disabled_files)
#Chat id's that will be ignored at runtime, edit to ignore permanently
#Across executions. Ex. [1234567, -9876543]
ignored_chats = []
