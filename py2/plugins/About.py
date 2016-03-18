from Plugin import Plugin

about_message = '''
Bot Written in *Python2*.
Also available in *Python3*.
Developed by @Sanguchi.
Source Code on [Github](github.com/sanguchi/GPB).
'''
class About(Plugin):

    def on_message(self, message):
        super(About, self).on_message(message)
        self.bot.send_message(self.cid, about_message, parse_mode = "Markdown")
        
    def get_help(self):
        return "about\nAbout this bot."
