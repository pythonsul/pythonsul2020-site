# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from decouple import config

AUTHOR = 'Python Sul'
SITENAME = 'Python Sul 2020'
SITEURL = config('SITE_URL', default='')

PATH = 'content'

PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['sitemap', ]

SITEMAP = {
    'format': 'xml',
    'exclude': [
        'tags.html', 'categories.html', 'authors.html', 'archives.html'
    ]
}
ARTICLE_ORDER_BY = 'date'
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt-br'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('2014', '#'),
    ('2015', '#'),
    ('2016', '#'),
    ('2018', '#'),
    ('2019', '#'),
)

# Social widget
SOCIAL = {
    'instagram': '',
    'twitter': 'https://www.twitter.com/pythonsul',
    'facebook': 'https://www.facebook.com/pythonsul',
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
