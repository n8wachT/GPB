from Plugin import Plugin
from requests import get
from lxml import etree

#key=[ODM4NDA]
cat_api = 'http://thecatapi.com/api/images/get?format=xml'

#xml.xpath('//response//data//images/*[1]/url/text()')[0]
xpath_string = '//response//data//images/*[1]/url/text()'

categories = [
'hats', 'space', 'funny', 'sunglasses', 'boxes', 'caturday', 
'ties', 'dream', 'kittens', 'sinks', 'clothes']

class Cat(Plugin):
    def on_start(self):
        self.api_key = self.load_value('api_key')
        if(not self.api_key):
            msg = 'Api key for thecatapi not found, please write / paste the token'
            self.api_key = self.ask_save(msg, str, 'api_key')
            
        #self.api_key = 'ODM4NDA'
        super(Cat, self).on_start()

    def on_message(self, message):
        super(Cat, self).on_message(message)
        if(self.rest):
            self.bot.reply_to(message, '[Link]({})'.format(get_cat(self.rest)), parse_mode='Markdown')
        else:
            self.bot.reply_to(message, '[Link]({})'.format(get_cat()), parse_mode='Markdown')
    def get_help(self):
        return '''
cat <category>
Returs a cat image, category is optional.
suported categories:
[{}]'''.format(' - '.join(categories))

def get_cat(query=None):
    if(query):
        if(query not in categories):
            return 'Bad Query!'
        return etree.fromstring(get(cat_api + '&category=' + query).text).xpath(xpath_string)[0]
    else:
        return etree.fromstring(get(cat_api).text).xpath(xpath_string)[0]
    return 'Something went wrong.'
