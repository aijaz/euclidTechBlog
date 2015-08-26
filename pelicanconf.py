#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Aijaz Ansari'
SITENAME = 'EuclidTech'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DELETE_OUTPUT_DIRECTORY = True

DEFAULT_PAGINATION = False

STATIC_PATHS = ['.', 'images', 'pdfs', 'js', 'css']
ARTICLE_PATHS = ['blog']
PAGE_PATHS = ['.']
TYPOGRIFY = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

THEME = '../pelican-themes/subtle'

#DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False
#
#MENUITEMS = (  ('About Us', '/about')
#             , ('Courses', '/courses')
#             , ('Contact', '/contact')
#            )


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
