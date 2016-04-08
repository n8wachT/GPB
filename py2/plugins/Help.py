from Plugin import Plugin
import Settings
class Help(Plugin):

    def on_message(self, message):
        super(Help, self).on_message(message)
        help_triggers = [self.get_name(), self.get_name() + '@' + Settings.username]
        if(message.text[1:] in help_triggers):
            self.bot.send_message(self.cid, self.build_help())
            return
        if(len(self.words) >= 2):
            query = self.words[1]
            for x in Settings.plugins:
                #print('testing [' + query + '] against [' + x.get_name() + ']')
                if(query == x.get_name()):
                    self.bot.send_message(self.cid, Settings.command_char + x.get_help())
                    return
            self.bot.send_message(self.cid, '[' + self.words[1] + '] not found.')

    def get_help(self):
        return "help <plugin>\nReturns help for plugin."
    def extract_help(self, plugin):
        return plugin.get_help()[:plugin.get_help().index('\n')]
    def build_help(self):
        result = []
        for x in Settings.plugins:
            help_string = self.extract_help(x)
            if(x.need_admin):
                help_string = help_string + '[*]'
            result.append(Settings.command_char + help_string)
        l = str(len(Settings.plugins))
        response = 'Detected Plugins: ' + l + '\n' + '\n'.join(result)
        return response + '\n[*] = Admins Only'
            
