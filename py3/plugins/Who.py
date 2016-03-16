from Plugin import Plugin

class Who(Plugin):
        
    def on_message(self, message):
        super().on_message(message)
        na, us, ui, gn, gi =(
        message.from_user.first_name,
        message.from_user.username,
        message.from_user.id,
        message.chat.username or message.chat.title or message.chat.first_name,
        message.chat.id)
        text = '''Info of {0}:
        👤 @{1}[{2}]
        👥 {3}[{4}]'''.format(na, us, ui, gn, gi)
        self.bot.send_message(self.cid, text)
        
    def get_help(self):
        return "Plugin that returns user data."
