# GPB
Generic Python2.7 Bot.

This bot uses [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

Install it with :
```
sudo pip install pyTelegramBotAPI
```

And clone the bot:
```
git clone https://github.com/sanguchi/GPB/
```
Don't forget to edit the token variable in Bot.py

###Creating Plugins.
1)Create a new python file inside 'plugins' folder.

2)Add the following line at start to import the Plugin superclass:
```python
from Plugin import Plugin
```
3)Define a class with the name of the plugin.
```python
class Hello(Plugin):
  pass
```
4)Implement `on_message(self, message)` method, there are two ways:

  4a)Use the `super(Hello, self).on_message(message)` method to get useful variables.
  ```python
    def on_message(self, message):
      super(Hello, self).on_message(message)
      self.bot.send_message(self.cid, "Hello!")
  ```
  4b)Just don't use `super().on_message(message)` and get the variables from `message`.
  ```python
    def on_message(self, message):
      self.bot.send_message(message.chat.id, "Hello!")
  ```
5)You can implement `get_help(self)` to get the help string of your plugin,
If you don't, the help string will return `'No description provided'`.
```python
  def get_help(self):
    return "A Plugin that says 'Hello!'."
```
5b)put this piece of code inside `on_message(self, message)` at the first:
```python
if(message.text[1:] == self.get_name()):
  self.bot.send_message(message.chat.id, self.get_help())
  return
```
6)Your plugin will look like this:
```python
from Plugin import Plugin

class Hello(Plugin):
  def on_message(self, message):
    super(Hello, self).on_message(message)
    if(message.text[1:] == self.get_name()):
      self.bot.send_message(self.cid, self.get_help())
      return
    self.bot.send_message(self.cid, "Hello!")

  def get_help(self):
    return "A Plugin that says 'Hello!'."
```
7)Save it with the name of the class, if your class is named `Hello`, your file must be called `Hello.py`.

8)Done! :D
