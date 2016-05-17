from Plugin import Plugin

class Kick(Plugin):
    def on_start(self):
        self.need_mod = True
        self.plugin_type = 'Management'
        return super(Kick, self).on_start()
        
    def on_message(self, message):
        super(Kick, self).on_message(message)
        if(message.reply_to_message and self.group):
            target_id = message.reply_to_message.from_user.id
            if(self.group.is_moderator(target_id)):
                self.bot.send_message(self.cid, 'Can\'t kick moderators.')
            if(self.group.admin == target_id):
                self.bot.send_message(self.cid, 'Can\'t kick Managers.')
            try:
                self.bot.kick_chat_member(self.cid, target_id)
                self.bot.unban_chat_member(self.cid, target_id)
            except Exception as e:
                self.bot.send_message(self.cid, 'An error has ocurred:\n%s' % e)
            
        if(len(self.words) == 2):
            try:
                target_id = int(self.words[1])
                self.bot.kick_chat_member(self.cid, target_id)
                self.bot.unban_chat_member(self.cid, target_id)
            except Exception as e:
                self.bot.send_message(self.cid, 'Something went wrong:\n%s' % e)
        if(len(self.words) == 1):
            self.bot.send_message(self.cid, self.get_help())
            
    def get_help(self):
        return "kick <id>\nKicks users by id or reply."
