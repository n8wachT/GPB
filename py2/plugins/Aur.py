from Plugin import Plugin
from json import loads
from requests import get

#deb_url = 'https://sources.debian.net/api/search/{}'
class Aur(Plugin):
    def on_start(self):
        super(Aur, self).on_start()

    def on_message(self, message):
        super(Aur, self).on_message(message)
        if(len(self.words) == 1):
            self.bot.reply_to(message, self.get_help())
        if(len(self.words) == 2):
            self.bot.reply_to(
            message, 
            search_package(self.words[1]), 
            disable_web_page_preview=True, 
            parse_mode="Markdown")
        else:
            self.bot.reply_to(message, 'Something went wrong')
    def get_help(self):
        return 'package\nSearch packages in AUR.'
        

def search_package(query):
    aur_url = 'https://aur.archlinux.org/rpc/?v=5&type=search&arg={}'
    query = str(query).encode('ascii', 'ignore').decode('ascii')
    print('Query = ' + query)
    if(len(query) < 2):
        return 'Invalid Query!'
    url = aur_url.format(query)
    res = loads(get(url).text)
    lines = []
    limit = 5
    if(res['resultcount'] == 0):
        return 'No results.'
    if(res['resultcount'] < 5):
        limit = res['resultcount']
    for x in range(limit):
        line = '*{}* - [URL]({})\n{}'.format(
        res['results'][x]['Name'], 
        res['results'][x]['URL'], 
        res['results'][x]['Description'])
        lines.append(line)
    return 'Results for {}\n{}'.format(query, '\n'.join(lines))
