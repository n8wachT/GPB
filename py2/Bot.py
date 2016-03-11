# -*- coding: utf-8 -*-
from Settings import *

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
    global plugins
    for p in plugins:
        #Fired on listening plugins
        if(p.listening):
            if(p.on_listen(m)):
                return
        #Fired on reply_to_message.
        if(m.reply_to_message and p.listening_reply):
            if(p.on_reply(m)):
                return
        if(m.text != None):
            if(m.text.split()[0][1:] in p.aliases):
                p.on_message(m)
                continue
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
