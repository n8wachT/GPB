from Plugin import Plugin

class Rank(Plugin):
    def on_start(self):
        self.need_mod = True
        self.plugin_type = 'Management'
        super(Rank, self).on_start()
        
    def on_message(self, message):
        super(Rank, self).on_message(message)
        if(message.reply_to_message and self.group):
            target_id = message.reply_to_message.from_user.id
            if(self.group.is_moderator(target_id)):
                self.bot.send_message(self.cid, self.group.del_moderator(target_id))
            else:
                self.bot.send_message(self.cid, self.group.add_moderator(target_id))
        else:
            self.bot.send_message(self.cid, 'Use this command by reply!')
        
    def get_help(self):
        return "rank\nRanks / Unrank an user, Manager only."
