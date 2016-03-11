# -*- coding: utf-8 -*-
import telebot
import Utils
token = ''
if(token == ''):
    token = input('No token detected, please paste or type here your token:\n> ')
print('token = ['+token+']')
bot = telebot.TeleBot(token)
plugins = Utils.build_plugins(bot, 'plugins')
command_char = '/'

###BOT RELATED STUFF

##Log messages to console.
def log_message(m):
    cid = m.chat.id
    if(m.content_type == 'text'):
        if cid > 0:
            name = m.chat.first_name.encode('ascii', 'ignore').decode('ascii')
            mensaje = name + "["+str(cid) + "]:" + m.text
        else:
            name = m.from_user.first_name.encode('ascii', 'ignore').decode('ascii')
            mensaje = name + "["+str(cid)+"]:"+ m.text
        print(mensaje.encode('ascii', 'ignore').decode('ascii'))
        
##Check if a message fires an event.
def fire_events(m):
    for p in plugins:
        if(m.text != None):
            #print('testing message ' + m.text + ' against plugin ' + p.get_name())
            if(m.text.startswith(command_char + p.get_name())):
                p.on_message(m)

#Custom listener.
def listener(messages):
    for m in messages:
        log_message(m)
        fire_events(m)
#Set custom listener.
bot.set_update_listener(listener)

print("Bot started")

#Bot starts here.
bot.polling(True)
