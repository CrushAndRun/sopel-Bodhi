# -*- coding: utf8 -*-
"""
giphy.py - Willie giphy Module
"""

from sopel.module import commands, example
import requests
import urllib
import re
import random

#https://github.com/Giphy/GiphyAPI

@commands('giphy')
@example('.giphy cat')
def giphy(bot, trigger):
    """.giphy cat"""
    API_KEY = bot.config.apikeys.giphy
    user_input = trigger.group(2)
    payload = {'api_key': API_KEY, 'q': user_input, 'offset': 0}
    r = requests.get("http://api.giphy.com/v1/gifs/search", params=payload)
    giphy_json = r.json()
    if giphy_json['pagination']['count'] > 0:
        rand_image = random.randint(0, giphy_json['pagination']['count'] - 1 )
        image_url = giphy_json['data'][rand_image]['images']['original']['url']
        bot.say(image_url)
    else:
        bot.say('No gif found. Blame bob')
