from Plugin import Plugin
from Settings import username
class Echo(Plugin):
        
    def on_message(self, message):
        super(Echo, self).on_message(message)
        #Check if there anything to reply
        echo_text = 'Nothing to echo.'
        if(len(self.words) == 1):
            if(message.reply_to_message and message.reply_to_message.text):
                echo_text = message.reply_to_message.text
            else:
                echo_text = self.get_help()
        else:
            echo_text = self.rest
        self.bot.send_message(self.cid, echo_text)
        
    def get_help(self):
        return "echo <text>\nA Simple Echo Plugin."
