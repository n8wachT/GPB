# -*- coding: utf-8 -*-
from Plugin import Plugin
from json import loads
from urllib2 import urlopen
from Utils import clean_markdown
import socket

class Geoip(Plugin):
        
    def on_message(self, message):
        super(Geoip, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        if(len(self.words) == 2):
            text_response = query_ip(self.words[1])
            #print('text_response:' + text_response)
            self.bot.send_message(self.cid, text_response, disable_web_page_preview=True, parse_mode="Markdown")
        
    def get_help(self):
        return "geoip <ip>\nReturns details about any given ip."

def query_ip(ip_string):
    ip = is_valid(ip_string)
    if(ip):
        url = 'http://geoip.nekudo.com/api/' + ip + '/short'
        response = urlopen(url).read()
        #print('Response:' + response)
        try:
            response = loads(response)
        except:
            return 'Invalid Response from server.'
        if('type' in response.keys()):
            if(response['type'] == 'error'):
                return 'Error : ' + response['msg']
        details = json_details(response)
        return u'\n'.join(details)
    else:
        return 'Invalid Query!'
        
def json_details(obj, tab=0):
    spaces = lambda(i): ' ' * i
    lines = []
    for key in obj:
        line = ''
        #print(u'key {} type : {}'.format(key, obj[key])
        if(type(obj[key]).__name__ == 'dict'):
            line = u'\n'.join(json_details(obj[key], tab + 1))
        else:
            line = u'*{}*: {}'.format(clean_markdown(key), clean_markdown(obj[key]))
        lines.append(spaces(tab) + line)
    return lines

#TODO: replace this shit with regex.
def is_valid(ip):
    try:
        data = socket.gethostbyname(ip)
        return str(data)
    except:
        return False
