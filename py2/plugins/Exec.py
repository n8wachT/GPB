from Plugin import Plugin
from Utils import catch_exception
import StringIO
import sys

def execute(string):
    cout = StringIO.StringIO()
    sys.stdout = cout
    try:
	exec(string)
    except Exception as e:
	print(catch_exception(e))
    if(cout.getvalue()):
	result = cout.getvalue()
    else:
	result = 'No output.'
    sys.stdout = sys.__stdout__
    return result
    
class Exec(Plugin):
        
    def on_message(self, message):
        super(Exec, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        result = execute(self.rest)
	result = '```\n' + result + '\n```'
	#print('result['+result+']')
        self.bot.send_message(self.cid, result, parse_mode = "Markdown")
        
    def get_help(self):
        return "exec <string>\nExecute strings as python statements."
