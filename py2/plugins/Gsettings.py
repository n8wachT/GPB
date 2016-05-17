from Plugin import Plugin

class Gsettings(Plugin):
    def on_start(self):
        self.need_mod = True
        self.plugin_type = 'Management'
        return super(Gsettings, self).on_start()
    
    def on_message(self, message):
        super(Gsettings, self).on_message(message)
        if(self.group):
            self.bot.send_message(self.cid, self.group_settings(self.group))
        
    def get_help(self):
        return "settings\nShows Group Settings."
        
    def get_name(self):
        return 'settings'
        
    def group_settings(self, group):
        text = '''
Group Settings:
Group ID: [{}] 
Manager ID:[{}]
Moderators Count: [{}]
Ignored Users Count: [{}]
Enabled Plugins:
{}
        '''.format(
        group.id,
        group.admin,
        len(group.moderators),
        len(group.ignored_users),
        '\n'.join(group.enabled_plugins))
        return text
        
        
        
        
