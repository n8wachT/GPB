import os, importlib, sys, traceback, urllib2
from json import loads
import Settings
def get_class(module):
    return module.__getattribute__(module.__name__.split('.')[1])

def get_modules(folder, disabled=[]):
    modules = []
    for x in os.listdir(folder):
        if(x.endswith('.py') and not 'init' in x and not x in disabled):
            module_name = folder + '.' + x.split('.')[0]
            #print('module name = ' + module_name)
            modules.append(importlib.import_module(module_name))
    return modules

def build_plugins(bot, folder, disabled=[]):
    plugins_list = []
    for x in get_modules(folder, disabled):
        plug = get_class(x)(bot)
        plugins_list.append(plug)
    return plugins_list
        
def call_later(function, seconds):
    pass

def catch_exception(exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = []
    for x in traceback.extract_tb(exc_tb).pop():
        tb.append(x)
    trace = 'File "{0}", line {1}, in {2}.'.format(tb.pop(0), tb.pop(0), tb.pop(0))
    message = '''Traceback (most recent call last):
    {0}
{1}: {2}.'''.format(trace, exc_type.__name__, exc_obj)
    #print('Exception Received, Message:\n' + message)
    return message

def get_document(file_id, filename):
    url_head = 'https://api.telegram.org/bot'
    url_method = '/getFile?file_id='
    full_url = url_head + Settings.token + url_method + file_id
    response = urllib2.urlopen(full_url).read()
    file_path = loads(response)['result']['file_path']
    file_url = 'https://api.telegram.org/file/bot{0}/{1}'.format(Settings.token, file_path)
    response = urllib2.urlopen(file_url).read()
    #print('Response = [{}]'.format(response))
    with open(filename, 'w') as plugin_file:
        plugin_file.write(response)
    return len(response)

