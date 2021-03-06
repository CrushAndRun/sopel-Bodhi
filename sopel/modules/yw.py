"""
welcome.py
Author: Enzo

So that the bot says "you're welcome" when thanked
"""

from __future__ import unicode_literals

import random
from sopel.module import rule

@rule(r'(?i)(thanks( a lot)?|thank you),? $nickname')
def yourewelcome(bot, trigger):
    reply = random.choice(('You\'re welcome', 'No problem', 'My pleasure', 'Any time'))
    punctuation = random.choice(('', '!'))
    bot.say(reply + ', ' + trigger.nick + punctuation)

@rule(r'(?i)(ty|tyvm),? $nickname')
def urwelcome(bot, trigger):
    reply = random.choice(('yw', 'yvw'))
    punctuation = random.choice(('', '!'))
    bot.say(reply + ', ' + trigger.nick + punctuation)
