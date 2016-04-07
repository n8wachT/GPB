import Settings
from Utils import catch_exception, change_line
#Base class for all plugins.
class Plugin(object):
    def __init__(self, bot):
        #Bot instance.
        self.bot = bot
        #Plugin Aliases, should be edited at on_start function.
        self.aliases = []
        #Used to fetch all messages.
        self.listening = False
        #Listen when a user replies to the bot.
        self.listening_reply = False
        #Set it to true if is a plugin only for admins.
        self.need_admin = False
        #Disable this plugin if it raises an exception.
        self.disable_on_error = True
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
        #Short for chat id
        self.cid = message.chat.id
        #Short for user id
        self.uid = message.from_user.id
        #Complete text of the message.
        self.text = message.text
        #Array with all the words.
        self.words = self.text.split()
        start_index = len(self.words[0])+len(Settings.command_char)
        #String with the rest of the message, except the command.
        self.rest = self.text[start_index:]

    #Function called when a message is listening to user reply.
    def on_reply(self, message):
        #Return False if the message should be propagated to another plugin listening.
        return False
    
    #Called when a message contain the alias / aliases for this plugin.    
    def on_alias(self, message):
        self.on_message(message)
        
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
