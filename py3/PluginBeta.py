#from Bot import command_char
class Plugin:
    def __init__(self, bot):
        self.bot = bot
        """
        possible_events: 
        'text', 'audio', 'document', 'photo',
        'sticker', 'video', 'voice', 'location',
        'contact', 'new_chat_participant', 'left_chat_participant',
        'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
        'group_chat_created'
        """
        self.possible_events = []
        self.custom_events = {}
        
    def get_name(self):
        return self.__class__.__name__

    def get_help(self):
        return 'No description provided'    
        
    def add_custom_event(self, function):
        self.custom_events[function.__name__] = function
            
    def fire_event(self, message, event = None):
        if(message.content_type in self.possible_events):
            return getattr(self, 'on_' + event)()
        elif(event in self.custom_events.keys()):
            return self.custom_events[event](message)
            
    ##CUSTOM EVENTS.
    def on_message(self, message):
        
        self.cid = message.chat.id
        self.uid = message.from_user.id
        self.text = message.text
        self.words = self.text.split()
        self.rest = self.text[len(self.get_name()):]
        #if(message.text == command_char + self.get_name()):
            #self.on_help(message)
        #fire_event(message)
        
    def on_help(self, message):
        bot.send_message(cid, get_help())
        
    def on_start(self, message):
        print(get_name(self) + ' Plugin started.')
        
    ##NORMAL EVENTS.    
    def on_text(self, message):
        pass
    
    def on_audio(self, message):
        pass
        
    def on_document(self, message):
        pass
        
    def on_photo(self, message):
        pass
        
    def on_sticker(self, message):
        pass
        
    def on_video(self, message):
        bot.send_message(message.chat.id, get_help())
        
    def on_voice(self, exception):
        pass
        
    def on_location(self, message):
        pass
        
    def on_contact(self, message):
        pass
        
    def on_new_chat_participant(self, message):
        pass
        
    def on_left_chat_participant(self, message):
        pass
        
    def on_new_chat_title(self, message):
        pass
        
    def on_new_chat_photo(self, message):
        pass
        
    def on_delete_chat_photo(self, message):
        pass
        
    def on_group_chat_created(self, message):
        pass
