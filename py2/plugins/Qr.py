# -*- coding: utf-8 -*-
from Plugin import Plugin
from requests import get
from requests.utils import quote
from tempfile import TemporaryFile

url = 'https://api.qrserver.com/v1/create-qr-code/?size=500x500&data='

class Qr(Plugin):
    def on_start(self):
        super(Qr, self).on_start()

    def on_message(self, message):
        super(Qr, self).on_message(message)
        if(self.rest):
            qr = get_qr(self.rest)
            if(qr):
                self.bot.send_photo(self.cid, open(qr, 'rb'), 'Qr image!.', message.message_id)
            else:
                self.bot.reply_to(message, 'Something went wrong.')
        else:
            self.bot.reply_to(message, '/' + self.get_help())
            
    def get_help(self):
        return 'qr <data>\nreturns a qr image from the given text.'
        
def get_qr(data):
    res = get(url + quote(data))
    if(res.status_code == 200):
        f = TemporaryFile(prefix='png')
        f.write(res.content)
        f.seek(0)
        return f
    else:
        return False
