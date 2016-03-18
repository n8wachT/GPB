from Plugin import Plugin

class Test(Plugin):

    def on_message(self, message):
        super(Test, self).on_message(message)
        self.bot.send_message(self.cid, 'Tested!')
        
    def get_help(self):
        return "test\nTest plugin."