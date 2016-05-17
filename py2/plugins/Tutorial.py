from Plugin import Plugin
from Statics import group_tutorial_message

class Tutorial(Plugin):
    def on_start(self):
        self.plugin_type = 'Basics'
        return super(Tutorial, self).on_start()
        
    def on_message(self, message):
        super(Tutorial, self).on_message(message)
        self.bot.send_message(self.cid, group_tutorial_message)
        
    def get_help(self):
        return "tutorial\nGet started with this plugin."
