from Plugin import Plugin
from Utils import kick_chat_member
class Kick(Plugin):
    def on_start(self):
        self.need_mod = True
        self.plugin_type = 'Management'
        super(Kick, self).on_start()
        
    def on_message(self, message):
        super(Kick, self).on_message(message)
        if(message.reply_to_message and self.group):
            target_id = message.reply_to_message.from_user.id
            if(self.group.is_moderator(target_id)):
                self.bot.send_message(self.cid, 'Can\'t kick moderators.')
            if(self.group.admin == target_id):
                self.bot.send_message(self.cid, 'Can\'t kick Managers.')
            res = kick_chat_member(self.cid, target_id)
            #self.bot.send_message(self.cid, str(res))
            if(not res['ok']):
                self.bot.send_message(self.cid, res['description'])
        if(len(self.words) == 2):
            try:
                target_id = int(self.words[1])
                res = kick_chat_member(self.cid, target_id)
                if(not res['ok']):
                    self.bot.send_message(self.cid, res['description'])
            except:
                self.bot.send_message(self.cid, 'Invalid Arguments')
        if(len(self.words) == 1):
            self.bot.send_message(self.cid, self.get_help())
    def get_help(self):
        return "kick <id>\nKicks users by id or reply."
