from Plugin import Plugin
import Settings
class Source(Plugin):
        
    def on_message(self, message):
        super(Source, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        if(len(self.words) == 2):
            plugin_name = self.words[1]
            for x in Settings.plugins:
                if(x.get_name() == plugin_name):
                    path = 'plugins/' + x.__class__.__name__ + '.py'
                    with open(path) as document:
                        self.bot.send_document(self.cid, document)
                    return
            self.bot.send_message(self.cid, 'Plugin {0} not found.'.format(plugin_name))
            
    def get_help(self):
        return "source <plugin>\nReturns the source file for the specified plugin."
