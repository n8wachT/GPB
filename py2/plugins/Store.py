from Plugin import Plugin
from Settings import command_char as ch
from Settings import server
class Store(Plugin):
    def on_start(self):
        self.aliases = ['add', 'get', 'del', 'json']
        print('character is['+ch+']')
        super(Store, self).on_start()

    def on_message(self, message):
        super(Store, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        elif(message.text == ch + 'json'):
            result = server.toggle_json()
            self.bot.send_message(self.cid, result)
            
        elif(message.text == ch + 'save'):
            result = server.save()
            print('Saving database')
            self.bot.send_message(self.cid, result)    
                    
        elif(len(self.words) == 2 and message.text.startswith(ch + 'get')):
            name = self.words[1]
            value = server.get_value(name)
            self.bot.send_message(self.cid, value)
        elif(len(self.words) == 2 and message.text.startswith(ch + 'del')):
            name = self.words[1]
            value = server.del_value(name)
            self.bot.send_message(self.cid, value)
        elif(len(self.words) == 3 and message.text.startswith(ch + 'add')):
            self.words.pop(0)
            name = self.words.pop(0)
            val = ' '.join(self.words)
            result = server.add_value(name, val)
            self.bot.send_message(self.cid, result)
        else:
            self.bot.send_message(self.cid, 'Invalid Arguments.')
        
    def get_help(self):
        return '''{0}get <name> | {0}del <name> | {0}add <name> <value> | {0}json | {0}save
        Store variables as <key> : <value>
        Usage:
            {0}add test tested
            {0}get test (will return tested)
            {0}del test
            {0}json     (on/off json mode)
            {0}save     (saves db to file)
        '''.format(ch)
