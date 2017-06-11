#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Burak Köse'
SITENAME = u'burakkose:blog'
SITEURL = 'http://koseburak.net'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'tr'

PYGMENTS_STYLE = 'trac'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

#GITHUB_USER = 'burakkose'
#GITHUB_SKIP_FORK = False

TWITTER_USERNAME = 'burakks41'
BANNER_SUBTITLE = """The way to succeed is to double your failure rate. Failure is the opportunity to begin again more intelligently.<br>
- Henry Ford, Ford Motor Company Founder"""
#CUSTOM_CSS = 'static/custom.css'

STATIC_PATHS = ['images', 'files', 'extra/robots.txt',
                'extra/favicon.ico', 'extra/custom.css']

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'}
}

# Blogroll
LINKS = None

# Social widget
SOCIAL = (('envelop', 'mailto:burakks41@gmail.com'),
          ('facebook', 'http://facebook.com/burakks41'),
          ('twitter', 'http://twitter.com/burakks41'),
          ('linkedin', 'http://www.linkedin.com/in/burakkose'),
          ('github', 'http://github.com/burakkose'),
          ('youtube', 'https://www.youtube.com/channel/UC6KivSaGWmirxNt2IyHFL0g'),
          ('skype', 'skype:ksv7r41?chat'),
          ('spotify', 'https://play.spotify.com/user/11138384529'),
          ('quora', 'https://www.quora.com/Burak-K%C3%B6se-1'),)

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

DEFAULT_PAGINATION = 10

TAG_CLOUD_MAX_ITEMS = 20

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = True

MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid']
THEME = 'theme/pelican-bootstrap3'

BOOTSTRAP_THEME = 'yeti'

BOOTSTRAP_NAVBAR_INVERSE = True

BANNER = 'images/banner.jpg'

#USE_OPEN_GRAPH = True
#OPEN_GRAPH_FB_APP_ID = ''
#OPEN_GRAPH_IMAGE = 'images/.png'
#TWITTER_CARDS = True

CC_LICENSE = "CC-BY-NC-SA"

PLUGIN_PATHS = ['plugins']

PLUGINS = ['just_table', 'tag_cloud', 'tipue_search',
           'optimize_images', 'pelican_gist']

DISQUS_SITENAME = 'koseburak'
GOOGLE_ANALYTICS = 'UA-56751819-1'
#ADDTHIS_PROFILE = ''

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags/'

DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
SHOW_ARTICLE_CATEGORY = True
