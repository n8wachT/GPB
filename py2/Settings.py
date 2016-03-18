import telebot
from Utils import build_plugins
#from SDBApi import SDBApi
#server = SDBApi()
admins = [59802458]
disabled_plugins = ['Store.py']
command_char = '!'
token = ''
if(token == ''):
    token = raw_input('No token detected, please paste or type here your token:\n> ')
print('token = ['+token+']')
bot = telebot.TeleBot(token)

plugins = build_plugins(bot, 'plugins', disabled_plugins)
