# -*- coding: utf-8 -*-
import json

default_plugins = ['plugins', 'rank', 'ignore', 'settings', 'help', 'echo', 'who', 'test']

class Group(object):
    def __init__(self, chat_id=0, admin_id=0):
        self.id = chat_id
        self.admin = admin_id
        self.moderators = []
        self.ignored_users = []
        self.banned_users = []
        self.custom_fields = {}
        self.enabled_plugins = default_plugins
        if(admin_id == 0):
            self.enabled_plugins.append('claim')
        print('New Group Settings created: id[{}], admin[{}]'.format(self.id, self.admin))
        
    def add_moderator(self, user_id):
        if(user_id in self.moderators):
            return 'This user is already a moderator.'
        if(user_id in self.ignored_users):
            return 'This user is in ignored users list, /ignore that user then /rank again.'
        if(user_id == self.admin):
            return 'Pfff, you\'re my admin, you can\'t make yourself a moderator.'
        self.moderators.append(user_id)
        return 'Added Moderator.'
    
    def del_moderator(self, user_id):
        if(user_id in self.moderators):
            self.moderators.remove(user_id)
            return 'User removed from Moderator List.'
        return 'User is not a moderator.'
    
    def add_ignore(self, user_id):
        if(user_id in self.ignored_users):
            return 'User is already ignored.'
        if(user_id in self.moderators):
            return 'Moderators can\'t be ignored, please /rank that user then /ignore again.'
        if(user_id == self.admin):
            return 'Nope, you\'re the Manager, you can\'t make me ignore you.'
        return 'Dafuq idk what happened with this error'
            
    def del_ignore(self, user_id):
        if(user_id in self.ignored_users):
            self.ignored_users.remove(user_id)
            return 'User removed from ignored list.'
        return 'User is not a ignored user.'
         
    def add_plugin(self, plugin_name):
        if(plugin_name in self.enabled_plugins):
            return 'Plugin is already enabled.'
        if(plugin_name in default_plugins):
            return 'You can\'t disable default plugins.'
        self.enabled_plugins.append(plugin_name)
        return 'Plugin Enabled.'
        
    def del_plugin(self, plugin_name):
        if(plugin_name in self.enabled_plugins):
            self.enabled_plugins.remove(plugin_name)
            return 'Plugin disabled.'
        return 'That Plugin isn\'t in the Enabled Plugins List of this Group'
    
    def is_moderator(self, user_id):
        return user_id in self.moderators
    
    def is_ignored(self, user_id):
        return user_id in self.ignored_users
        
    def has_field(self, field_name):
        return field_name in self.custom_fields
    
    def to_dict(self):
        table = {}
        table['id'] = self.id
        table['admin'] = self.admin
        table['moderators'] = self.moderators
        table['ignored_users'] = self.ignored_users
        table['custom_fields'] = self.custom_fields
        table['enabled_plugins'] = self.enabled_plugins
        table['banned_users'] = self.banned_users
        return table

    def from_dict(self, table):
        self.id = table['id']
        self.admin = table['admin']
        self.moderators = table['moderators']
        self.ignored_users = table['ignored_users']
        self.custom_fields = table['custom_fields']
        self.enabled_plugins = table['enabled_plugins']
        self.banned_users = table['banned_users']
        print('Group loaded from dict: id[{}], admin[{}]'.format(self.id, self.admin))
        
    def from_json(self, json_string):
        table = json.loads(json_string)
        from_dict(self, table)
        #self.id = table['id']
        #self.admin = table['admin']
        #self.moderators = table['moderators']
        #self.ignored_users = table['ignored_users']
        #self.custom_fields = table['custom_fields']
        #self.enabled_plugins = table['enabled_plugins']
        #self.banned_users = table['banned_users']
        print('Group loaded from json: id[{}], admin[{}]'.format(self.id, self.admin))
