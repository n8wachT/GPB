# -*- coding: utf-8 -*-
from Plugin import Plugin
import feedparser
from Utils import clean_markdown
class Feed(Plugin):
    def on_start(self):
        super(Feed, self).on_start()

    def on_message(self, message):
        super(Feed, self).on_message(message)
        if(self.rest):
            self.bot.reply_to(
            message, 
            get_feed(self.rest), 
            disable_web_page_preview=True, 
            parse_mode="HTML")
        else:
            self.bot.reply_to(message, self.get_help())
    def get_help(self):
        return 'feed <url>\nReturns first 5 links on the given rss url.'


#CODE TAKEN FROM:
#https://gist.github.com/Jeshwanth/99cf05f4477ab0161349        
def get_feed(url):
    try:
        feed = feedparser.parse(url)
    except:
        return 'Invalid url.'
    y = len(feed[ "items" ])
    y = 5 if y > 5 else y
    if(y < 1):
        return 'Nothing found'
    lines = ['<b>Feed:</b>'] 
    for x in range(y):
        lines.append(
        u'-&gt <a href="{1}">{0}</a>.'.format(
        u'' + feed[ "items" ][x][ "title" ], 
        u'' + feed[ "items" ][x][ "link" ]))
    return u'' + '\n'.join(lines)
