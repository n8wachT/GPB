from Plugin import Plugin

class Manage(Plugin):
    def on_start(self):
        self.need_mod = True
        return super(Manage, self).on_start()
        
    def on_message(self, message):
        super(Manage, self).on_message(message)
        self.bot.send_message(self.cid, 'This plugin is on development, don\'t use it yet.')
        
    def get_help(self):
        return "manage\nCommand to setup the bot."
