# -*- coding: utf-8 -*-
from Plugin import Plugin
from urllib2 import urlopen


class Pbin(Plugin):

    def on_message(self, message):
        super(Pbin, self).on_message(message)
        self.bot.send_message(self.cid, get_trending() , disable_web_page_preview=True, parse_mode="Markdown")
        
    def get_help(self):
        return "pbin\nReturns Trending pastes from pastebin."

def get_trending():
    url = 'http://pastebin.com/trends'
    response = urlopen(url).read()
    start_text = '<td><img src="/i/t.gif"  class="i_p0" alt="" /><a href="'
    end_text = '</a></td>'
    pastes = []
    pastes.append(u'6 most popular pastes created in the last 72 hours.')
    cursor = 0
    for x in range(6):
        cursor = response.index(start_text, cursor + 1) + len(start_text)
        link = u'http://pastebin.com' + response[cursor:cursor + 9]
        cursor += 11
        name = response[cursor:response.index(end_text, cursor)].decode('utf-8')
        result = u'*{0}* - [link]({1}).'.format(
        name,
        link)
        pastes.append(result)
    result = '\n'.join(pastes)
    #print('result =[{}]'.format(result))
    return result
    
#<td><img src="/i/t.gif"  class="i_p0" alt="" /><a href="/bQ7wYngV">‪#‎OpWhiteRose</a></td>
