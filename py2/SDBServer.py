# -*- coding: utf-8 -*-
import json
from os.path import exists

class SDBServer:
    def __init__(self, json_mode=False):
        self.variables = {}
        self.json_mode = json_mode
        print('Server started, json_mode = ' + str(self.json_mode))
        
    def add_value(self, name, value):
        self.variables[name] = value
        if(self.json_mode):
            result = json.dumps({name : self.variables[name]})
        else:
            result = 'added [' + name + '], value = ' + value
        return result
        
    def del_value(self, name):
        try:
            val = self.variables.pop(name)
            if(self.json_mode):
                result = json.dumps({name : val})
            else:
                result = '[' + name + '] removed.'
            return result
        except KeyError:
            if(self.json_mode):
                result = json.dumps({name : None})
            else:
                result = '[' + name + '] not found.'
            return result

    def get_value(self, name):
        try:
            if(self.json_mode):
                return json.dumps({name : self.variables[name]})
            else:
                return '[' + name + '] = ' + self.variables[name]
        except KeyError:
            if(self.json_mode):
                return json.dumps({name : None})
            else:
                return '[' + name + '] not found.'

    def get_all(self):
        if(self.json_mode):
            return json.dumps(self.variables)
        else:
            if(len(self.variables) == 0):
                return '[empty]'
            result = ''
            for x in self.variables:
                result = result + '[' + x + '] = ' + self.variables[x] + '\n'
        return result
    
    def save(self):
        with open('SDBS.db', 'w') as f:
            json.dump(self.variables, f)
        print('Database Saved.')
        if(self.json_mode):
            return json.dumps({'Saved' : True})
        else:
            return 'DB file saved.'
    def load(self):
        if exists('SDBS.db'):
            with open('SDBS.db', ) as f:
                variables = json.load(f)
            if(self.json_mode):
                return json.dumps({'loaded': True})
            else:
                return '[loaded] = True'
        else:
            with open('SDBS.db','w') as f:
                json.dump({}, f) 
            if(self.json_mode):
                return json.dumps({'created': True})
            else:
                return '[created] = True'
    def json(self):
        self.json_mode = not self.json_mode
        if(self.json_mode):
            return json.dumps({'json_mode': True})
        else:
            return '[json_mode] = False'
            
def start(json_mode=False):
    return SDBServer(json_mode)
