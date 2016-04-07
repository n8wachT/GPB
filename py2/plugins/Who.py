from Plugin import Plugin

class Who(Plugin):

    def on_message(self, message):
        super(Who, self).on_message(message)
        self.bot.send_message(self.cid, user_info(message))

    def get_help(self):
        return "who\nPlugin that returns user data."
    
def user_info(message):
    pemji = u'\U0001f464'
    gemji = u'\U0001f465'
    if message.reply_to_message:
        fname = message.reply_to_message.from_user.first_name
        usrid = str(message.reply_to_message.from_user.id)
        uname = message.reply_to_message.from_user.username or 'He doesn\'t have username!'
        grpid = str(message.reply_to_message.chat.id)
        gname = message.reply_to_message.chat.title or 'No chat title!'
        gunme = message.chat.username or gname
        msgfm = u'Info about {}:\n{} @{}[{}]\n{} {}[{}]'.format(fname, pemji, uname, usrid, gemji, gname, grpid)
        if message.reply_to_message.chat.type == 'group':
            return msgfm
        if message.reply_to_message.chat.type == 'supergroup':
            return msgfm
    fname = message.from_user.first_name
    usrid = str(message.from_user.id)
    uname = message.from_user.username or 'You don\'t have username!'
    grpid = str(message.chat.id)
    gname = message.chat.title or 'No chat title!'
    gunme = message.chat.username or gname
    msgfm = u'Info about {}:\n{} @{}[{}]\n{} {}[{}]'.format(fname, pemji, uname, usrid, gemji, gname, grpid)
    if message.chat.type == 'private':
        return u'Info about {}:\n{} @{}[{}]'.format(fname, pemji, uname, usrid)
    if message.chat.type == 'group':
        return msgfm
    if message.chat.type == 'supergroup':
        return msgfm
    return 'No Info'
