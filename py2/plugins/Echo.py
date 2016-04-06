from Plugin import Plugin

class Echo(Plugin):
        
    def on_message(self, message):
        super(Echo, self).on_message(message)
        if(len(self.words) == 1):
            self.bot.send_message(self.cid, self.get_help())
            return
        self.bot.send_message(self.cid, self.rest)
        
    def get_help(self):
        return "echo <text>\nA Simple Echo Plugin."
