from Plugin import Plugin
from subprocess import Popen, PIPE
from Utils import clean_markdown

class Shell(Plugin):
    def on_start(self):
        self.need_admin = True
        self.hidden = True
        super(Shell, self).on_start()
        
    def on_message(self, message):
        super(Shell, self).on_message(message)
        #Check if there anything to reply
        result_text = clean_markdown(Popen(self.rest, stdout=PIPE).communicate()[0])
        self.bot.reply_to(message, '```' + result_text + '```' ,parse_mode='Markdown')
        
    def get_help(self):
        return "shell <text>\nExecutes given string with system shell."
