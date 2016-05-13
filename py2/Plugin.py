# -*- coding: utf-8 -*-
import Settings
from Utils import catch_exception, change_line, get_group, ask
from Store import get_cursor, get_dbconn
#Base class for all plugins.
class Plugin(object):
    def __init__(self, bot):
        #Bot instance.
        self.bot = bot
        #DEPRECATED, I THINK ALIASES ARE USELESS.
        #(but i leave it here if you want to use them.)
        #Plugin Aliases, should be edited at on_start function.
        self.aliases = []
        #Used to fetch all messages.
        self.listening = False
        #Listen when a user replies to the bot.
        self.listening_reply = False
        #Set it to true if is a plugin only for admins(the bot's owner).
        self.need_admin = False
        #Set it to true if is a moderation/management plugin.
        self.need_mod = False
        #Disable this plugin if it raises an exception.
        self.disable_on_error = True
        #Set it to true to make it unavaliable to certain bots functions.
        self.hidden = False
        #Set it to true to make a plugin only available for private chats.
        self.private_only = False
        #Edit this if you want to make your plugin appear in plugin_market.
        self.plugin_type = 'Undefined'
        #Customize your plugin inside this function.
        self.on_start()
        
    #Returns the plugin name in lowercase based on class .    
    def get_name(self):
        return self.__class__.__name__.lower()
    #Generic help message. Must be overriden by plugins.
    def get_help(self):
        return 'No description provided'    
            
    ##PLUGIN EVENTS.
    #Customize your plugin overriding this function.
    def on_start(self):
        print(self.get_name() + ' Plugin started.')
    
    #Called when a message contains the plugin name.
    def on_message(self, message):
        print('Plugin ' + self.get_name() + ' fired.')
        #Short for chat id
        self.cid = message.chat.id
        #Short for user id
        self.uid = message.from_user.id
        #Complete text of the message.
        self.text = message.text
        #Array with all the words.
        self.words = self.text.split()
        #String with the rest of the message, except the command.
        self.rest = self.text.split(' ', 1)[1] if len(self.words) > 1 else False
        #Current Group Instance.
        #group can be false if the current chat is not a group chat
        #or if chat id is not in the groups table.
        self.group = get_group(self.cid)

    #Function called when a message is listening to user reply.
    def on_reply(self, message):
        #Return False if the message should be propagated to another plugin listening.
        return False
        
    #DEPRECATED. DON'T USE ALIASES, I THINK THERE ARE USELESS.
    #Called when a message contain the alias / aliases for this plugin.
    #Override it to let know a plugin when is called by their alias/es
    def on_alias(self, message):
        self.on_message(message)
        #Return False if the message should be propagated to the rest of plugins.
        #So you can call multiple plugins with the same alias at once.
        return False
        
    #Called when a plugin sets listening to True. This is called for all messages.
    def on_listen(self, message):
        #Return False if the message should be propagated to the rest of listening plugins.
        return False
    
    #Called on plugin's errors, override this if you want handle the exceptions.
    def on_error(self, message, exception):
        #First try to send the exception via telegram.
        text = catch_exception(exception)
        if(Settings.strict_errors):
            text = ('\nWARNING, STRICT PLUGIN DISABLING ON ERRORS IS ENABLED.\n' +
                    'THIS PLUGIN WILL BE DISABLED ACROSS EXECUTIONS\n' +
                    'TO RE-ENABLE THIS PLUGIN JUST EDIT Settings.py\n' +
                    text)
        else:
            text = text + '\nAdvice: This plugin has been disabled at runtime.'
        try:
            self.bot.send_message(message.chat.id, '```{}```'.format(text), parse_mode='Markdown')
        #If not, print the exception on console.
        except:
            print(text)
        #Default behavior: disable the plugin.
        #Override the on_error function if you don't want your plugin to be disabled.
        name = self.get_name()
        for x in Settings.plugins:
            if(x.get_name() == name):
                p = Settings.plugins.pop(Settings.plugins.index(x))
                Settings.disabled_plugins.append(p)
                #This disables permanently the plugin across executions.
                if(Settings.strict_errors):
                    filename = p.__class__.__name__ + '.py'
                    cline = "disabled_files = ['" + "', '".join(Settings.disabled_files) + "']\n"
                    nline = "disabled_files = ['" + "', '".join(Settings.disabled_files) + "', '" + filename + "']\n"
                    change_line('Settings.py', cline, nline)
                    
    #Save a value into database.
    def add_value(self, variable, value):
        script = 'insert into plugins(plugin, variable, value) values(?, ?, ?);'
        cur = get_cursor()
        cur.execute(script, (self.get_name(), variable, value))
        get_dbconn().commit()
            
    #Load a value from database, if there is not such value, return default value.
    def load_value(self, variable, default=None):
        script = '''select value from plugins where plugin='{}' and variable='{}';'''
        script = script.format(self.get_name(), variable)
        cur = get_cursor()
        val = cur.execute(script).fetchone()
        return val[0] if val else default
    
    def update_value(self, variable, value):
        script = '''
replace into plugins values(?, ?, ?) 
union select plugin, variable, from plugins
where plugin='{}' and variable='{}'
'''.format(self.get_name(), variable)
        cur = get_cursor()
        cur.execute(script, (self.get_name(), variable, value))
        get_dbconn().commit()
            
    def ask_save(self, msg, obj, variable):
        script = 'insert into plugins(plugin, variable, value) values(?, ?, ?);'
        cur = get_cursor()
        cur.execute(script, (self.get_name(), variable, ask(msg, obj)))
        get_dbconn().commit()
        return variable
