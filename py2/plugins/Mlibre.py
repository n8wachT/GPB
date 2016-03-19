# -*- coding: utf-8 -*-
from Plugin import Plugin
from json import loads
from urllib2 import urlopen

class Mlibre(Plugin):

    def on_message(self, message):
        super(Mlibre, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        query = self.rest.replace(' ', '%20')
        result = request_ml(query)
        self.bot.send_message(self.cid, result , disable_web_page_preview=True, parse_mode="Markdown")
        
    def get_help(self):
        return "mlibre <query>\nReturns 'Mercado Libre Argentina' search results."

def request_ml(query):
    results = []
    url = 'https://api.mercadolibre.com/sites/MLA/search?q=' + query
    response = loads(urlopen(url).read())
    if(response['paging']['total'] == 0):
        return '*No results*'
    if(response['paging']['total'] < 5):
        max_range = response['paging']['total']
    else:
        max_range = 5
    for i in range(max_range):
        item = response['results'][i]
        result = u'{0}\n*${1}* - {3} - [link]({2}).'.format(
        item['title'],
        item['price'],
        item['permalink'],
        item['address']['city_name'])
        results.append(result)
        
    return '\n'.join(results)
