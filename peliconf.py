#!/usr/bin/env python
# coding: utf-8

AUTHOR = 'Marshall Ward'
SITENAME = "Marshall's Blog"
SITEURL = 'http://marshallward.org'
TIMEZONE = 'Australia/Canberra'
LOCALE = 'C'

STATIC_PATHS = ['images']

DEFAULT_PAGINATION = 4

MARKUP = ('rst')
DEFAULT_CATEGORY = 'Other'

SOCIAL = (
            ('Google+', 'https://plus.google.com/u/0/114191722446820072187'),
            ('Twitter', 'http://twitter.com/marshall_ward'),
            ('github', 'http://github.com/marshallward'),
            ('flickr', 'http://www.flickr.com/photos/marshallward/')
         )

# MaWa theme variables
# (Maybe move these to pelican?)

from pelican import __version__
PELICAN_VERSION = __version__

from datetime import datetime
BUILD_DATE = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
