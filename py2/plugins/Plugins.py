# -*- coding: utf-8 -*-
from Plugin import Plugin
from Utils import build_plugins, get_document
import Settings
help_message = "plugins <argument> [plugin]\n" + (
'''Dinamic Plugin Manager.
Arguments:
write <name> - Write a plugin 'on the fly'.
disable [plugin] - Disables the desired plugin.
enable [plugin] - Re-Enable the plugin.
reload - Re-scans the plugins folder.
upload - Create a plugin by file.
update [plugin] - Updates plugin's code.
''')

class Plugins(Plugin):
    
    def on_start(self):
        self.need_admin = True
        return super(Plugins, self).on_start()
        
    def on_message(self, message):
        super(Plugins, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
        if(len(self.words) == 3):
            arg = self.words[1]
            opt = self.words[2]
            if(arg == 'write'):
                self.write_plugin(opt)
            elif(arg == 'disable'):
                self.disable_plugin(opt)
            elif(arg == 'enable'):
                self.enable_plugin(opt)
            elif(arg == 'update'):
                self.update_plugin(opt)
            elif(arg == 'add'):
                if(self.group):
                    self.bot.reply_to(message, self.group.add_plugin(opt))
                else:
                    self.bot.reply_to(message, 'This only work in groups.')
            elif(arg == 'remove'):
                if(self.group):
                    self.bot.reply_to(message, self.group.del_plugin(opt))
                else:
                    self.bot.reply_to(message, 'This only work in groups.')
            else:
                self.bot.reply_to(message, 'Invalid Arguments')
        if(len(self.words) == 2):
            arg = self.words[1]
            if(arg == 'reload'):
                self.reload_plugins()
            elif(arg == 'upload'):
                self.upload_plugin()
            else:
                self.bot.reply_to(message, 'Bad Arguments')
            
    def get_help(self):
        return help_message
        
    def write_plugin(self, name):
        write_message = 'write:'+name+'\n' + (
        'Reply to this message with your source code.\n' + 
        'It will be saved as ' + name + '.py')
        self.bot.send_message(self.cid, write_message)
        self.listening_reply = True
        
    def disable_plugin(self, name):
        for x in Settings.plugins:
            if(x.get_name() == name):
                p = Settings.plugins.pop(Settings.plugins.index(x))
                Settings.disabled_plugins.append(p)
                self.bot.send_message(self.cid, 'Plugin ' + name + ' disabled.')
                return
        self.bot.send_message(self.cid, 'Plugin ' + name + ' not found.')

    def enable_plugin(self, name):
        for x in Settings.disabled_plugins:
            if(x.get_name() == name):
                p = Settings.disabled_plugins.pop(Settings.disabled_plugins.index(x))
                Settings.plugins.append(p)
                self.bot.send_message(self.cid, 'Plugin ' + name + ' enabled.')
                return
        self.bot.send_message(self.cid, 'Plugin ' + name + ' not found.')
        
    def update_plugin(self, name):
        self.bot.send_message(self.cid, 'Command not implemented yet.')
        
    def upload_plugin(self):
        write_message = 'code:upload\n' + (
        'Reply to this message with your .py file')
        self.bot.send_message(self.cid, write_message)
        self.listening_reply = True
        
    def on_reply(self, message):
        code = message.reply_to_message.text.split('\n')[0]
        if(code.startswith('write')):
            name = 'plugins/' + code.split(':')[1] + '.py'
            write_to_file(name, message.text)
            self.bot.send_message(message.chat.id, 'Saved {0} bytes in {1}.'.format(len(message.text), name))
            self.listening_reply = False
            return True
        if(code.startswith('code:upload')):
            if(not message.document):
                self.bot.reply_to(message, 'I need a .py File, please restart Again.')
                return False
            if(not message.document.file_name.endswith('.py')):
                self.bot.reply_to(message, 'Only .py Files, please restart Again.')
                return False
            name = 'plugins/'+message.document.file_name
            written_bytes = get_document(message.document.file_id, name)
            self.bot.send_message(message.chat.id, 'Written {0} bytes in {1}.'.format(written_bytes, name))
            self.listening_reply = False
            return True
        return False

    def reload_plugins(self):
        dis = Settings.disabled_plugins
        plugins_list = build_plugins(Settings.bot, 'plugins', dis)
        diff = len(plugins_list) - len(Settings.plugins)
        Settings.plugins = plugins_list
        self.bot.send_message(self.cid, '{0} news plugins found.'.format(diff))
        return diff
        
def write_to_file(name, text):
    with open(name, 'w') as f:
        f.write(text)
