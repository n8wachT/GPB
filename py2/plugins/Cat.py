from Plugin import Plugin
#key=[ODM4NDA]
class Cat(Plugin):
    def on_start(self):
        super(Cat, self).on_start()

    def on_message(self, message):
        super(Cat, self).on_message(message)

    def get_help(self):
        return 'cat <query>\nReturs a cat image, query is optional.'
