import telebot
import Utils
from SDBApi import SDBApi
server = SDBApi()
command_char = '/'
token = ''
if(token == ''):
    token = raw_input('No token detected, please paste or type here your token:\n> ')
print('token = ['+token+']')
bot = telebot.TeleBot(token)
plugins = Utils.build_plugins(bot, 'plugins')
