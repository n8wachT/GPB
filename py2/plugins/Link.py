from Plugin import Plugin
from Settings import username

class Link(Plugin):
        
    def on_message(self, message):
        super(Link, self).on_message(message)
        triggers = [self.get_name(), self.get_name() + '@' + username]
        if(message.text[1:] in triggers):
            self.bot.send_message(self.cid, self.get_help())
            return
        if(len(self.words) == 3):
            #text_link = u'[' + self.words[1] + '](' + self.words[2] + ')'
            #print('text_link:' + text_link) 
            text_link = u'[{}]({})'.format(self.words[1], self.words[2])
            try:
                self.bot.send_message(self.cid, text_link, disable_web_page_preview=True, parse_mode="Markdown")
            except:
                self.bot.send_message(self.cid, 'Don\'t fool me, rat kid.')
        elif(len(self.words) == 2 and message.reply_to_message):
            if(message.reply_to_message.text):
                text_link = u'[{}]({})'.format(self.words[1], message.reply_to_message.text)
                try:
                    self.bot.send_message(self.cid, text_link, disable_web_page_preview=True, parse_mode="Markdown")
                except:
                    self.bot.send_message(self.cid, 'Don\'t fool me, rat kid.')
        else:
            self.bot.send_message(self.cid, 'Your argument is invalid.')

    def get_help(self):
        return "link <text> <link>\nReturns a clicable text with the given link."
