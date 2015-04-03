"""
Constants that may be used in multiple packages
"""
try:
    from collections import OrderedDict
except ImportError, exc:
    # Python 2.6.
    from ordereddict import OrderedDict

from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Message type selector.
LOCAL_MESSAGE, EMAIL_MESSAGE, NO_MESSAGES, DEFAULT_MESSAGES, ALL_MESSAGES = range(5)

MESSAGING_MAP = OrderedDict([
    (DEFAULT_MESSAGES, _("default"),),
    (LOCAL_MESSAGE, _("local messages"),),
    (EMAIL_MESSAGE, _("email"),),
    (ALL_MESSAGES, _("email for every new thread (mailing list mode)")),
])

MESSAGING_TYPE_CHOICES = MESSAGING_MAP.items()

# Connects a user sort dropdown word to a data model field.
USER_SORT_MAP = OrderedDict([
    (_("recent visit"), "-profile__last_login"),
    (_("reputation"), "-score"),
    (_("date joined"), "profile__date_joined"),
    #("number of posts", "-score"),
    (_("activity level"), "-activity"),
])

# These are the fields rendered in the user sort order drop down.
USER_SORT_FIELDS = USER_SORT_MAP.keys()
USER_SORT_DEFAULT = USER_SORT_FIELDS[0]

USER_SORT_INVALID_MSG = "Invalid sort parameter received"

# Connects a post sort dropdown word to a data model field.
POST_SORT_MAP = OrderedDict([
    (_("update"), "-lastedit_date"),
    (_("views"), "-view_count"),
    (_("followers"), "-subs_count"),
    (_("answers"), "-reply_count"),
    (_("bookmarks"), "-book_count"),
    (_("votes"), "-vote_count"),
    (_("rank"), "-rank"),
    (_("creation"), "-creation_date"),
])

# These are the fields rendered in the post sort order drop down.
POST_SORT_FIELDS = POST_SORT_MAP.keys()
POST_SORT_DEFAULT = POST_SORT_FIELDS[0]

POST_SORT_INVALID_MSG = "Invalid sort parameter received"

# Connects a word to a number of days
POST_LIMIT_MAP = OrderedDict([
    (_("all time"), 0),
    (_("today"), 1),
    (_("this week"), 7),
    (_("this month"), 30),
    (_("this year"), 365),

])

# These are the fields rendered in the time limit drop down.
POST_LIMIT_FIELDS = POST_LIMIT_MAP.keys()
POST_LIMIT_DEFAULT = POST_LIMIT_FIELDS[0]

POST_LIMIT_INVALID_MSG = _("Invalid limit parameter received")


def now():
    return datetime.utcnow().replace(tzinfo=utc)


