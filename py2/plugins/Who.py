from Plugin import Plugin

class Who(Plugin):

    def on_message(self, message):
        super(Who, self).on_message(message)
        na, us, ui, gi = (
        message.from_user.first_name,
        message.from_user.username,
        str(message.from_user.id),
        str(message.chat.id))
        pe = u'\U0001f464'
        ge = u'\U0001f465'
        if(message.chat.username):
            gn = '@' + message.chat.username
        else:
            gn = message.chat.title or message.chat.first_name
        text = 'Info of ' + na + ':\n' + pe + ' @'+us+'['+ui+']\n'+pe+ ' ' + gn + '['+gi+']'
        #text = '''Info of {0}:
        #{5} @{1}[{2}]
        #{6} {3}[{4}]'''.format(na, us, ui, gn, gi, pe, ge)
        self.bot.send_message(self.cid, text)

    def get_help(self):
        return "who\nPlugin that returns user data."
