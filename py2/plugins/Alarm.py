from Plugin import Plugin
from time import sleep, time
from threading import Thread

def to_seconds(string):
    if(string[len(string) - 1:] in ['s', 'm', 'h']):
        unit = string[len(string) - 1:]
        scnd = string[:len(string) - 1]
        try:
            if(unit == 's'):
                return float(scnd)
            elif(unit == 'm'):
                return float(scnd) * 60
            elif(unit == 'h'):
                return float(scnd) * 60 * 60
        except ValueError:
            return None
    else:
        try:
            return float(string) * 60
        except ValueError:
            return None


class Reminder():
    def __init__(self, unix_time, chat_id, text_message):
        self.time = unix_time
        self.cid = chat_id
        self.text = text_message
        
class Alarm(Plugin):
    def on_start(self):
        self.reminders = []
        self.hilo = Thread(target=self.check_loop)
        self.running = True
        self.hilo.daemon = True
        self.hilo.start()
        print('Alarm thread started')
        return super(Alarm, self).on_start()
        
    def on_message(self, message):
        super(Alarm, self).on_message(message)
        if(message.text[1:] == self.get_name()):
            self.bot.send_message(self.cid, self.get_help())
            return
        if(len(self.words) >= 3):
            self.words.pop(0)
            time_arg = self.words.pop(0)
            seconds = to_seconds(time_arg)
            if(seconds):
                message = ' '.join(self.words)
                remind = Reminder(int(time() + seconds), self.cid, message)
                self.reminders.append(remind)
                if(time_arg.endswith('s')):
                    delay = str(int(seconds)) + ' seconds'
                elif(time_arg.endswith('m')):
                    delay = str(int(seconds/60)) + ' minutes'
                elif(time_arg.endswith('h')):
                    delay = str(int((seconds/60) / 60)) + ' hours'
                else:
                    delay = str(int(seconds/60)) + ' minutes'
                self.bot.send_message(self.cid,
                'Alarm set for {0} from now.\nMessage:[{1}]'.format(delay, message))
            else:
                self.bot.send_message(self.cid, 'Your Argument is invalid.')
                
                
    def get_help(self):
        return "alarm <time> <text>\nAlarm plugin.\nTime units: s|m|h, default: m."


    def check_loop(self):
        while(self.running):
            now = time()
            for x in self.reminders:
                if(x.time < now):
                    self.bot.send_message(x.cid, x.text)
                    self.reminders.pop(self.reminders.index(x))
            sleep(1)
