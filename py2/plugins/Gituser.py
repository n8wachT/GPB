from Plugin import Plugin
from json import loads
from requests import get

class Gituser(Plugin):
    def on_start(self):
        super(Gituser, self).on_start()

    def on_message(self, message):
        super(Gituser, self).on_message(message)
        if(len(self.words) == 1):
            self.bot.reply_to(message, get_help())
            return
        if(len(self.words) == 2):
            self.bot.reply_to(
            message, 
            gituser_repos(self.words[1]), 
            disable_web_page_preview=True, 
            parse_mode="Markdown")
        else:
            self.bot.reply_to(message, 'Invalid Arguments')

    def get_help(self):
        return 'gituser <user>\nReturns information about user\'s repositories.'
        
def gituser_repos(user):
    user = str(user).encode('ascii', 'ignore').decode('ascii')
    if(len(user) < 4):
        return 'Invalid Query!'
    api_url = 'https://api.github.com/users/{}/repos'.format(user)
    res = loads(get(api_url).text)
    if(res.__class__.__name__ != 'list'):
        return res['message']
    lines = []
    star = 'Stars'
    for x in res:
        line = u'_{}_ - *{}* - Stars: {}\n{} - [clone]({})'.format(
        x['language'],
        x['name'],
        x['stargazers_count'],
        x['description'],
        x['clone_url'])
        if(x['fork']):
            line = u'{} - *{}*(`fork`) - Stars: {}\n{} - [clone]({})'.format(
            x['language'],
            x['name'],
            x['stargazers_count'],
            x['description'],
            x['clone_url'])
        lines.append(line)
    return '{} repositories:\n{}'.format(user, '\n'.join(lines))
        
