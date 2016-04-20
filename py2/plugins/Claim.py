# -*- coding: utf-8 -*-
from Plugin import Plugin
from Settings import username, command_char, groups
from Utils import get_group, save_groups

claim_message = u'''
Group {} with id {} have been Claimed by:
User {} with id {}.
Now you're the Bot's Manager.
type /tutorial to get started.
'''

class Claim(Plugin):
        
    def on_message(self, message):
        super(Claim, self).on_message(message)
        if(message.reply_to_message):
            print('Reply Passed')
            if(message.reply_to_message.from_user.username == username):
                print('Reply To Username Passed')
                if(message.text == command_char + 'claim@' + username):
                    print('Full Command text passed')
                    if(self.group):
                        self.group.admin = message.from_user.id
                        self.group.enabled_plugins.remove('claim')
                        name = u'' + message.from_user.first_name#.encode('utf-8')#.decode('utf-8')
                        title = u'' + message.chat.title#.encode('utf-8')#.decode('utf-8')
                        self.bot.send_message(self.cid, claim_message.format(title,message.chat.id, name, self.group.admin))
                        save_groups(groups)
                    else:
                        self.bot.reply_to(message, 'Error, Self.group not found')
                else:
                    self.bot.reply_to(message, 'Full Command not passed,expected:[{}]received:[{}]'.format(command_char + 'claim@' + username, message.text))
            else:
                self.bot.reply_to(message, 'Reply To Username requeriment not passed')
        else:
            self.bot.reply_to(message, 'Reply requeriment don\'t passed.')
            
    def get_help(self):
        return "claim <text>\nTurns you the bot's manager if the group isn't registered in the database."
