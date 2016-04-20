# -*- coding: utf-8 -*-
import Settings
from Events import message_event
bot = Settings.bot
###BOT RELATED STUFF

##Log messages to console.
def log_message(m):
    cid = m.chat.id
    name = m.from_user.first_name.encode('ascii', 'ignore').decode('ascii')
    if(m.content_type == 'text'):
        message_text = m.text.encode('ascii', 'ignore').decode('ascii')
        #name = m.chat.first_name if cid > 0 else m.from_user.first_name
    else:
        message_text = m.content_type
    print('{}[{}]:{}'.format(name, cid, message_text))
        
#Custom listener.
def listener(messages):
    for m in messages:
        if(m.chat.id in Settings.ignored_chats):
            continue
        log_message(m)
        message_event(m)
        
#Set custom listener.
bot.set_update_listener(listener)

print("Bot started")
for admin in Settings.admins:
    bot.send_message(admin, 'Bot Started.')
#Bot starts here.
bot.polling(True)
