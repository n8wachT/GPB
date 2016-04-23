from Plugin import Plugin
from random import choice

class Stickers(Plugin):
    def on_start(self):
        self.sticker_list = []
        self.listening = True
        super(Stickers, self).on_start()

    def on_message(self, message):
        super(Stickers, self).on_message(message)
        self.bot.send_sticker(self.cid, choice(self.sticker_list), reply_to_message_id=message.message_id)
    def get_help(self):
        return 'stickers\nReplies with a random sticker'
    
    def on_listen(self, message):
        if(message.content_type == 'sticker'):
            self.sticker_list.append(message.sticker.file_id)
            print('Sticker added, file_id:', message.sticker.file_id)
        return False
