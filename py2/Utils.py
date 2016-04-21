# -*- coding: utf-8 -*-
import os, importlib, sys, traceback, json
from requests import get
import Settings
from Group import Group
####BOT UTILS

#Extract a class named equals to the module.
def get_class(module):
    return module.__getattribute__(module.__name__.split('.')[1])
    
#Extract modules from a folder.
def get_modules(folder, disabled=[]):
    modules = []
    for x in os.listdir(folder):
        if(x.endswith('.py') and not 'init' in x and not x in disabled):
            module_name = folder + '.' + x.split('.')[0]
            #print('module name = ' + module_name)
            modules.append(importlib.import_module(module_name))
    return modules

#Returns an array with plugin instances.
def build_plugins(bot, folder, disabled=[]):
    plugins_list = []
    for x in get_modules(folder, disabled):
        plug = get_class(x)(bot)
        plugins_list.append(plug)
    return plugins_list

#Downloads files from telegram and saves it with a given pathname
def get_document(file_id, filename):
    url_head = 'https://api.telegram.org/bot'
    url_method = '/getFile?file_id='
    full_url = url_head + Settings.token + url_method + file_id
    response = get(full_url).text
    file_path = json.loads(response)['result']['file_path']
    file_url = 'https://api.telegram.org/file/bot{0}/{1}'.format(Settings.token, file_path)
    response = get(file_url).text
    #print('Response = [{}]'.format(response))
    with open(filename, 'w') as plugin_file:
        plugin_file.write(response)
    return len(response)
    
#Clean markdown characters from the given string.
def clean_markdown(text):
    text = u'' + str(text)
    text = text.replace('_', ' ')
    text = text.replace('*', '')
    text = text.replace('`', '')
    return text

#escape html.    
def escape_tags(text):
    text = u'' + str(text)
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

#### GENERIC UTILS

#TODO: Make a utility to call a function after x seconds.
def call_later(function, seconds):
    pass
    
#Handle Generic exceptions and return a text with the information.
def catch_exception(exception):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    tb = []
    for x in traceback.extract_tb(exc_tb).pop():
        tb.append(x)
    trace = 'File "{0}", line {1}, in {2}.'.format(tb.pop(0), tb.pop(0), tb.pop(0))
    message = '''
Traceback (most recent call last):
    {0}
{1}: {2}.'''.format(trace, exc_type.__name__, exc_obj)
    #print('Exception Received, Message:\n' + message)
    return message

#Utility to change a certain line from a file to another text.
def change_line(target_file, original_line, modified_line):
    #print('Target File[{0}]\nOriginal Line[{1}]\nModified Line[{2}].'.format(
    #target_file, original_line, modified_line))
    this = open(target_file)
    lines = this.readlines()
    this.close()
    this = open(target_file, 'w')
    for x in lines:
        if(x == original_line):
            #print('Original[{0}] - Modified[{1}].'.format(x, modified_line))
            x = modified_line
        this.write(x)
    this.close()
    #print('Absolute Path[{}]'.format(os.path.abspath(target_file)))


### GROUP UTILS

gfile = 'groups.json'

def init_groups():
    if os.path.exists(gfile):
        with open(gfile) as f:
            groups_table = json.load(f)
    else:
        with open(gfile,'w') as f:
            json.dump({}, f)
            return {}
    groups = []
    for x in groups_table:
        g = Group()
        g.from_dict(x)
        groups.append(g)
    print('Groups Array Initialized, {} groups loaded.'.format(len(groups)))
    return groups

def save_groups(groups):
    groups_table = []
    for x in groups:
        groups_table.append(x.to_dict())
    with open(gfile, 'w') as f:
        json.dump(groups_table, f)
    print('groups.json saved.')
        
def get_group(chat_id):
    for x in Settings.groups:
        if(chat_id == x.id):
            return x
    return False

#Check plugin required privileges against user privileges.
#PD: CHECK YOUR PRIVILEGES FAM.
def check_privileges(u, g, p):
    privilege_level = 0
    privilege_required = 0
    if(u.__class__.__name__ == 'int'):
        uid = u
    else:
        uid = u.from_user.id
        
    if(uid in g.moderators):
        privilege_level += 1
    if(uid == g.admin):
        privilege_level += 1
    if(uid in Settings.admins):
        privilege_level += 1
    if(p.need_mod):
        privilege_required += 1
    if(p.need_admin):
        privilege_required += 2
    can = privilege_level >= privilege_required
    return can


##CUSTOM BOT UTILS
def kick_chat_member(chat_id, user_id):
    url = 'https://api.telegram.org/bot{}/kickChatMember?chat_id={}&user_id={}'.format(
    Settings.token, chat_id, user_id)
    response = get(url).text
    return json.loads(response)
