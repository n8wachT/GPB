import os
import importlib

def get_class(module):
    return module.__getattribute__(module.__name__.split('.')[1])

def get_modules(folder):
    modules = []
    for x in os.listdir(folder):
        if(x.endswith('.py') and not 'init' in x):
            module_name = folder + '.' + x.split('.')[0]
            #print('module name = ' + module_name)
            modules.append(importlib.import_module(module_name))
    return modules

def build_plugins(bot, folder):
    plugins_list = []
    for x in get_modules(folder):
        plug = get_class(x)(bot)
        plugins_list.append(plug)
    return plugins_list
        
def call_later(function, seconds):
    pass
