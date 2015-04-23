# -*- coding: utf8 -*-
from biostar.settings.base import *

SITE_DOMAIN = "tetrad.xyz"
SERVER_EMAIL = "tetradxyz@gmail.com"

# Override any other settings that you might need
# See the biostars/settings/base.py for settings options

DATABASE_NAME = get_env("DATABASE_NAME")
DATABASE_USER = get_env("DATABASE_USER")
DATABASE_PASSWORD = get_env("DATABASE_PASSWORD")

DEBUG = True

# Template debug mode.
TEMPLATE_DEBUG = True

# Should the django compressor be used.
USE_COMPRESSOR = False

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

START_CATEGORIES = [
    "Новые",  "Открытые",
]

# These should be the most frequent (or special) tags on the site.
NAVBAR_TAGS = [
    "Задачи", "Вопросы",
]

# The last categories. These tags have special meaning internally.
END_CATEGORIES = [
    # "Задачи", "Вопросы",
]

# These are the tags that always show up in the tag recommendation dropdown.
POST_TAG_LIST = NAVBAR_TAGS

# This will form the navbar
CATEGORIES = START_CATEGORIES + NAVBAR_TAGS + END_CATEGORIES

# This will appear as a top banner.
# It should point to a template that will be included.
TOP_BANNER = ""

EMAIL_USE_TLS = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'