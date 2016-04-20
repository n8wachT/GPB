from Plugin import Plugin
from libraries.chatterbotapi import ChatterBotFactory, ChatterBotType
from Settings import command_char, me, username
class Chat(Plugin):
    def on_start(self):
        self.factory = ChatterBotFactory()
        self.bot1 = self.factory.create(ChatterBotType.CLEVERBOT)
        self.bot1session = self.bot1.create_session()
        self.bot2 = self.factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
        self.bot2session = self.bot2.create_session()
        self.hidden = True
        self.listening = True
        super(Chat, self).on_start()
            
    def chat(self, text_message):
        try:
            res = self.bot1session.think(text_message)
            return res
        except:
            try:
                res = self.bot2session.think(text_message)
                return res
            except:
                return '...?'

    def on_listen(self, message):
        if(message.text):
            if(message.text.startswith(command_char)):
                return False
            else:
                mtext = message.text.lower()
                if(mtext.find(username.lower()) > 0
                or mtext.find(me.first_name.lower()) > 0
                or mtext.find(me.first_name.lower()[1:]) > 0
                or (message.reply_to_message and message.reply_to_message.from_user.username == username)):
                    print('Chatter plugin fired.')
                    self.bot.reply_to(message, self.chat(message.text), parse_mode='HTML')
            
