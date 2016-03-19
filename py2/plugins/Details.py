# -*- coding: utf-8 -*-
from Plugin import Plugin

class Details(Plugin):
        
    def on_message(self, message):
        super(Details, self).on_message(message)
        reply = message.reply_to_message
        if(reply):
            self.bot.send_message(self.cid, get_details(reply), parse_mode="HTML")
        else:
            self.bot.send_message(self.cid, 'Please use the command with a reply message.')
            
    def get_help(self):
        return "details\nShows info about a message."

def get_details(obj, tab=0):
    spaces = lambda(i): ' ' * i
    ommited_types = ['instancemethod', 'function', 'builtin_function_or_method']
    attributes = []
    for x in dir(obj):
        if(not x.startswith('__')):
            name = u'<code>{}</code>'.format(clean_string(x))
            attribute = getattr(obj, x)
            value = clean_string(getattr(obj, x))
            if(type(attribute).__name__ in ommited_types):
                continue
            if(type(attribute).__name__ == 'instance'):
                attribute = '{\n' + get_details(attribute, tab + 4) + '}'
            elif(type(attribute).__name__ == 'list'):
                attribute = '{\n' + get_details(attribute[0], tab + 4) + '}'
            else:
                attribute = '<b>' + clean_string(attribute) + '</b>'
            #print(u'{0} = {1}'.format(x, attribute))
            text = u'{0} = {1}'.format(name, attribute)
            attributes.append(spaces(tab) + text)
    return '\n'.join(attributes)
    
def clean_string(string):
    rstring = u'{}'.format(string)
    rstring.replace('>', '')
    rstring.replace('<', '')
    return rstring
