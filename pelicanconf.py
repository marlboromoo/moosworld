#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'marlboromoo'
SITENAME = u"Moo's World"
SITEURL = 'http://127.0.0.1:8000'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'utf8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('AchievementsGen1', 'https://amunak.net/projects/mcachievements/'),
          ('AchievementsGen2', 'http://mcgen.menzerath.eu/'),
          ('AwesomeSkins', 'http://mctools.tyzoid.com/skins/'),
          ('Bahamut', 'http://forum.gamer.com.tw/C.php?bsn=18673&snA=70656&tnum=2&subbsn=4'),
          ('CraftBukkit', 'http://bukkit.org/'),
          ('Komica', 'http://komica.peroneko.org/minecraft/'),
          ('Minebot', 'http://minebot.net/'),
          ('Minecraft', 'http://www.minecraft.net/'),
          ('Minecraft Wiki', 'http://zh.minecraftwiki.net/Minecraft_Wiki'),
          ('Mojang | Support Center', 'http://help.mojang.com/'),
          ('Moo\'s World', 'http://moosmcworld.blogspot.tw/'),
          ('Moo\'s World II', 'http://moosbook.blogspot.tw/'),
          ('SignatureCraft', 'http://signaturecraft.us/'),
          ('Skin Viewer', 'http://minecraft.aggenkeech.com/'),
          ('Textcraft', 'http://textcraft.net/'),)

# Social widget
#SOCIAL = (('twitter', '#'),
#          ('github', '#'),
#          ('rss', '#'),
#         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = True

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DROPDOWN_MENU = True
DROPDOWN_MENUITEMS = {
    'Server' : (
        ('DynMap', 'http://dynmap.moosworld.net'),
        ('Map', 'http://map.moosworld.net'),
        ('MCBans', 'http://mcbans.com/server/40833/play.moosworld.net/bans/')
    ),
    'Mods' : (
        ('Download', 'http://download.moosworld.net'),
    )
}
MENUITEMS = (
)

# Theme
THEME = '/home/timothylee/project/pelican-bootstrap3/'
#BOOTSTRAP_THEME = 'readable'
