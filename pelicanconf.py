#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'marlboromoo'
SITENAME = u"Moo's World"
#SITEURL = 'http://127.0.0.1:8000'
#SITEURL = 'http://marlboromoo.github.io/moosworld'
SITEURL = 'http://moosworld.net'


TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'utf8'

# Brand
FAVICON = 'images/favicon.ico'
#SITEBRAND = 'images/MoosWorld_silver.png'

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
    'Chat' : (
        ('moosworld2@kekeke.cc', 'http://kekeke.cc/moosworld2'),
        ('#moosworld.net@irc.esper.net', 'http://irc.moosworld.net/'),
    ),
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
BLOCKS = (
    ('Server', 'fa-cloud', """IP: play.moosworld.net:25565 <div id="web_mcstatus-container">Loading ...</div>
<script src="http://mcstatus.moosworld.net/web_mcstatus.js?host=play.moosworld.net" type="text/javascript"></script> """),
    ('Donate', 'fa-usd', """
    <p>如果你覺得Moo's world帶給你很多樂趣, 或想要更好的遊戲品質, 非常歡迎實質上的支持! 多種的贊助方式可選擇:</p>
    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" class="form-inline">
       <input type="hidden" name="cmd" value="_s-xclick" />
       <input type="hidden" name="hosted_button_id" value="JLK9YM6J2F87W" />
       <input type="hidden" name="on0" value="I love Moo&#39;s World" />
       <select name="os0" class="form-control">
          <option value="Stone" />Stone $5.00
          <option value="Iron" />Iron $10.00
          <option value="Gold" />Gold $20.00
          <option value="Diamond" />Diamond $50.00
       </select>
       <input type="hidden" name="currency_code" value="USD" />
       <input type="submit" value="GO" class="btn btn-default"/>
       <span class="help-block">(使用Paypal贊助, 單位 USD.)</span>
    </form>
    <form name="donate_atm" class="form-inline">
         <select name="menu" class="form-control">
            <option value="https://ecbank.com.tw/order/express.php?method=vacc&mer_id=6915&amt=150&expire_day=15&item_desc=I%20love%20Moo%27s%20World%20-%20Stone" />Stone $150
            <option value="https://ecbank.com.tw/order/express.php?method=vacc&mer_id=6915&amt=300&expire_day=15&item_desc=I%20love%20Moo%27s%20World%20-%20Iron" />Iron $300
            <option value="https://ecbank.com.tw/order/express.php?method=vacc&mer_id=6915&amt=600&expire_day=15&item_desc=I%20love%20Moo%27s%20World%20-%20Gold" />Gold $600
            <option value="https://ecbank.com.tw/order/express.php?method=vacc&mer_id=6915&amt=1500&expire_day=15&item_desc=I%20love%20Moo%27s%20World%20-%20Diamond" />Diamond $1500
            </select>
            <input type="button" id="button" class="btn btn-default"
            onclick="window.open(document.donate_atm.menu.options[document.donate_atm.menu.selectedIndex].value);" value="GO" />
        <span class="help-block">(使用ATM贊助, 單位 NTD.)</span>
     </form>
<form name="donate_barcode" class="form-inline">
         <select name="menu" class="form-control">
            <option value="https://ecbank.com.tw/order/express.php?method=barcode&amp;mer_id=6915&amp;amt=150&amp;expire_day=15&amp;item_desc=I%20love%20Moo%27s%20World%20-%20Stone" />Stone $150
            <option value="https://ecbank.com.tw/order/express.php?method=barcode&amp;mer_id=6915&amp;amt=300&amp;expire_day=15&amp;item_desc=I%20love%20Moo%27s%20World%20-%20Iron" />Iron $300
            <option value="https://ecbank.com.tw/order/express.php?method=barcode&amp;mer_id=6915&amp;amt=600&amp;expire_day=15&amp;item_desc=I%20love%20Moo%27s%20World%20-%20Gold" />Gold $600
            <option value="https://ecbank.com.tw/order/express.php?method=barcode&amp;mer_id=6915&amp;amt=1500&amp;expire_day=15&amp;item_desc=I%20love%20Moo%27s%20World%20-%20Diamond" />Diamond $1500
            </select>
            <input type="button" id="button" class="btn btn-default"
            onclick="window.open(document.donate_barcode.menu.options[document.donate_barcode.menu.selectedIndex].value);" value="GO" />
            <span class="help-block">(使用超商條碼贊助, 單位 NTD.)</span>
     </form>
     """),
)

# Comment
DISQUS_SITENAME = 'moosworld'
DISQUS_DISPLAY_COUNTS = False

# Social
#GITHUB_USER = 'marlboromoo'

# Theme
THEME = './pelican-bootstrap3/'
#BOOTSTRAP_THEME = 'spacelab'
#BOOTSTRAP_THEME = 'cyborg'
BOOTSTRAP_THEME = 'readable-old'

