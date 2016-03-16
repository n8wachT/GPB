from Plugin import Plugin

class Bold(Plugin):

    def on_message(self, message):
        super(Bold, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        self.bot.send_message(self.cid,'*' + self.rest + '*', parse_mode = "Markdown")
        
    def get_help(self):
        return "bold <text>\nReturns bold text."
