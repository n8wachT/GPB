# -*- coding: utf-8 -*-
import Settings
bot = Settings.bot
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
    for p in Settings.plugins:
        #Fired on listening Plugins
        if(p.listening):
            if(p.on_listen(m)):
                return
        #Fired on reply_to_message.
        if(m.reply_to_message and p.listening_reply):
            if(p.on_reply(m)):
                return
        #Text messages section.
        if(m.text != None):
            #Fired on Alias
            if(m.text.split()[0][1:] in p.aliases):
                #Check if is an admin plugin.
                if(p.need_admin and m.from_user.id not in Settings.admins):
                    bot.reply_to(m, 'Admin Only.')
                    return
                try:
                    p.on_message(m)
                except Exception as e:
                    p.on_error(m, e)
                continue
            #Fired on Plugin Name
            if(m.text.startswith(Settings.command_char + p.get_name())):
                #Check if is an admin plugin.
                if(p.need_admin and m.from_user.id not in Settings.admins):
                    bot.reply_to(m, 'Admin Only.')
                    return
                try:
                    p.on_message(m)
                except Exception as e:
                    p.on_error(m, e)

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
