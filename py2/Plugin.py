class Plugin(object):
    def __init__(self, bot):
        self.bot = bot
        self.aliases = []
        self.listening = False
        self.listening_reply = False
        self.need_admin = False
        self.need_root = False
        self.on_start()
        
    def get_name(self):
        #print('name:[' + self.__class__.__name__.lower() + ']')
        return self.__class__.__name__.lower()

    def get_help(self):
        return 'No description provided'    
            
    ##CUSTOM EVENTS.
    def on_start(self):
        print(self.get_name() + ' Plugin started.')

    def on_message(self, message):
        self.cid = message.chat.id
        self.uid = message.from_user.id
        self.text = message.text
        self.words = self.text.split()
        self.rest = self.text[len(self.get_name())+2:]

    def on_reply(self, message):
        return False
        
    def on_listen(self, message):
        return False
        
    def on_error(self, exception):
        pass
