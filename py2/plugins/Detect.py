# -*- coding: utf-8 -*-
from Plugin import Plugin
from libraries.face_eyes import detect_eyes, detect_faces
from Utils import get_binary
from os import unlink

#Plugin section.
class Detect(Plugin):
    
    def on_start(self):
        super(Detect, self).on_start()
        
    def on_message(self, message):
        super(Detect, self).on_message(message)
        if(message.reply_to_message):
            if(message.reply_to_message.photo):
                self.detect(message)
            else:
                self.bot.reply_to(message, 'Use with an image!')
        else:
            self.bot.reply_to(message, 'Use by reply!')
        
    def get_help(self):
        return 'detect <query>\nNo description provided.'
        
    def detect(self, message):
        f_id = None
        b_size = 0
        for p in message.reply_to_message.photo:
            t_size = p.height * p.width
            if t_size > b_size:
                b_size = t_size
                f_id = p.file_id
        fname = 'downloads/' + f_id + '.jpg'
        fname = str(fname)
        get_binary(f_id, fname)
        fcs = detect_faces(fname)
        eys = detect_eyes(fname)
        if(fcs == 0 and eys == 0):
            unlink(fname)
            return self.bot.reply_to(message, 'No faces or eyes found.') 
        caption = 'Found {} face{} and {} eye{}.'.format(
        fcs, ('s' if fcs == 1 else ''), eys, ('s' if eys == 1 else ''))
        self.bot.send_photo(self.cid, open(fname, 'rb'), caption, message.message_id)
        unlink(fname)
        
