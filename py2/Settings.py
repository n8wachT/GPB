import telebot
from Utils import build_plugins
#from SDBApi import SDBApi
#server = SDBApi()
admins = [59802458]
disabled_files = ['Store.py']
disabled_plugins = []
strict_errors = False
command_char = '/'
token = ''
if(token == ''):
    token = raw_input('No token detected, please paste or type here your token:\n> ')
print('token = ['+token+']')
bot = telebot.TeleBot(token)
username = bot.get_me().username
print('Bot username: [@' + username + ']')
print('Command char: [' + command_char + ']')
plugins = build_plugins(bot, 'plugins', disabled_files)
