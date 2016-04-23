# -*- coding: utf-8 -*-
import Settings, Statics
from Utils import check_privileges, save_groups, kick_chat_member
from Group import Group
###GROUP CHAT EVENTS


def plugin_list(group):
    plugin_list = []
    #print('Checking Plugins against the {} plugins of group {}.'.format(len(group.enabled_plugins), group.id))
    for x in Settings.plugins:
        if(x.get_name() in group.enabled_plugins):
            plugin_list.append(x)
    #print('Plugin list returned size: ' + str(len(plugin_list)))
    return plugin_list


def group_invited(m):
    g = Group(m.chat.id, m.from_user.id)
    Settings.groups.append(g)
    name = m.from_user.first_name
    msg = Statics.group_invited_message.format(name.encode('utf-8'), m.from_user.id)
    Settings.bot.send_message(m.chat.id, msg)
    save_groups(Settings.groups)


def group_event(m, group):
    #print('Group event fired!')
    group_plugins = plugin_list(group)
    #print('Group Plugins size:' + str(len(group_plugins)))
    ##LISTEN EVENTS.
    #Fires on_listen event for listening plugins.
    for plugin in group_plugins:
        if(plugin.listening and check_privileges(m, group, plugin)):
            if(plugin.on_listen(m)):
                return

    ##REPLY EVENTS.

    if(m.reply_to_message):
        #Fires on_reply event for a plugin expecting a user reply.
        for plugin in group_plugins:
            if(plugin.listening_reply and check_privileges(m, group, plugin)):
                if(plugin.on_reply(m)):
                    return

    ##TEXT EVENTS.
    if(m.text):
        first_word = m.text.split()[0][1:]
        #print('word:[{}]'.format(first_word))
        #DEPRECATED BECAUSE I THINK THIS IS USELESS.
        #Also is still usable...
        #Fires on_alias event for a plugin with one or more aliases.
        for plugin in group_plugins:
            if(not m.text.startswith(Settings.command_char)):
                return
            #print('Command = ' + first_word)
            if(first_word in plugin.aliases and check_privileges(m, group, plugin)):
                if(plugin.on_alias(m)):
                    return
            if(first_word == plugin.get_name() and check_privileges(m, group, plugin)):
                try:
                    plugin.on_message(m)
                    return
                except Exception as e:
                    plugin.on_error(m, e)
                    return
        
        #-------ADMIN SECTION--------
        if(m.from_user.id in Settings.admins):
            for x in Settings.plugins:
                if(m.text.startswith(Settings.command_char + x.get_name())):
                    try:
                        x.on_message(m)
                    except Exception as e:
                        x.on_error(m, e)
        #-------ADMIN SECTION--------
def group_expulsed(m):
    for admin in Settings.admins:
        Settings.bot.send_message(admin, 'Bot expulsed from chat [{}].'.format(m.chat.id))
    
    for group in Settings.groups:
        if(group.id == m.chat.id):
            Settings.groups.remove(group)
    print('Bot expulsed from chat [{}].'.format(m.chat.id))

    
def group_glitch(m):
    g = Group(m.chat.id, 0)
    Settings.groups.append(g)
    Settings.bot.send_message(m.chat.id, Statics.group_glitch_message)
    

#Bind message to group.
def group_select(m):
    #Event Fired when the bot is invited to a group.
    if(m.new_chat_participant and m.new_chat_participant.username == Settings.username):
        group_invited(m)
        return
    #Event Fired when the bot is removed from group.
    if(m.left_chat_participant and m.left_chat_participant.username == Settings.username):
        group_expulsed(m)
        return
    #Normal Events for groups.
    for x in Settings.groups:
        if(x.id == m.chat.id):
            group_event(m, x)
            return
    
    #Rare case, when the bot detects is already in a group not registered in groups list.
    group_glitch(m)
    #g = Group(m.chat.id, m.from_user.id)
    #Settings.groups.append(g)

        
###PRIVATE CHATS EVENTS
def chat_created(m):
    pass

def chat_blocked(m):
    pass

def chat_event(m):
        ##TEXT EVENTS.
    if(m.text):
        #-------ADMIN SECTION--------
        if(m.from_user.id in Settings.admins):
            for x in Settings.plugins:
                if(m.text.startswith(Settings.command_char + x.get_name())):
                    try:
                        x.on_message(m)
                    except Exception as e:
                        x.on_error(m, e)
        #-------ADMIN SECTION--------
def chat_glitch(m):
    pass

def private_select(m):
    if(m.chat.id in Settings.admins):
        chat_event(m)
    
def message_event(m):
    if(m.chat.type == 'private'):
        private_select(m)
        return
    elif(m.chat.type == 'group'):
        group_select(m)
        return
    else:
        Settings.bot.send_message(m.chat.id, 'This bot is not implemented to work in {} yet.'.format(m.chat.type))
        kick_chat_member(m.chat.id, Settings.me.id)
        #Settings.ignored_chats.append(m.chat.id)
