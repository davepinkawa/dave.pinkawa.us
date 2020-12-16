#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dave Pinkawa'
SITENAME = 'pinkawa.us'
SITEURL = 'https://dave.pinkawa.us'
#SITEURL = ''
SITETITLE = 'Play, Teach, Learn'
SITESUBTITLE = "Dave Pinkawa's Personal Blog"
SITEDESCRIPTION = "Dave Pinkawa's Thoughts and Writings"
COPYRIGHT_YEAR = 2020

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

# Social widget
SOCIAL = (
    ('envelope', 'mailto:dave@pinkawa.us'),
    ('github', 'https://github.com/davepinkawa'),
    ('linkedin','https://www.linkedin.com/in/david-pinkawa/'),
    ('twitter','https://twitter.com/davepinkawa'),
)

MENUITEMS = (
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags')
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

# 256491466

DISQUS_SITENAME = 'dave-pinkawa-us'
GOOGLE_ANALYTICS = '256491466'