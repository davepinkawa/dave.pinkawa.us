#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dave Pinkawa'
SITENAME = 'pinkawa.us'
SITEURL = 'https://dave.pinkawa.us'
#SITEURL = ''
SITETITLE = 'Play, Teach, Learn'
SITESUBTITLE = "Dave Pinkawa's Personal Blog"
SITEDESCRIPTION = "Dave Pinkawa's Thoughts and Writings"
COPYRIGHT_YEAR = 2021

MAIN_MENU = True
SITELOGO = SITEURL + "/images/favicon.ico"
FAVICON = SITEURL + "/images/favicon.ico"
PATH = 'content'
THEME = 'theme/Flex-2.4.0'
TIMEZONE = 'America/Chicago'

ROBOTS = "index, follow"
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', '/'),)
SUMMARY_MAX_LENGTH = 30

# Social widget
SOCIAL = (
    ('envelope', 'mailto:dave@pinkawa.us'),
    ('github', 'https://github.com/davepinkawa'),
    ('linkedin','https://www.linkedin.com/in/david-pinkawa/'),
    ('twitter','https://twitter.com/davepinkawa'),
    ("rss", "/feeds/all.atom.xml"),
)

MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html')
)

DEFAULT_PAGINATION = 10

#PLUGIN_PATHS = ['/where/you/cloned/it/pelican-plugins/', ]
PLUGINS=['sitemap',]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

DISQUS_SITENAME = 'dave-pinkawa-us'
GOOGLE_ANALYTICS = 'G-LGDSDJGSDJ'