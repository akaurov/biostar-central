from .models import Award, AwardDef, Badge

from biostar.apps.posts.models import Post, Vote
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import utc
from datetime import datetime, timedelta


def now():
    return datetime.utcnow().replace(tzinfo=utc)


def wrap_list(obj, cond):
    return [obj] if cond else []

# Award definitions
AUTOBIO = AwardDef(
    name=_("Autobiographer"),
    desc=_("has more than 80 characters in the information field of the user's profile"),
    func=lambda user: wrap_list(user, len(user.profile.info) > 80),
    icon="fa fa-bullhorn"
)

GOOD_QUESTION = AwardDef(
    name=_("Good Question"),
    desc=_("asked a question that was upvoted at least 5 times"),
    func=lambda user: Post.objects.filter(vote_count__gt=5, author=user, type=Post.QUESTION),
    icon="fa fa-question"
)

GOOD_ANSWER = AwardDef(
    name=_("Good Answer"),
    desc=_("created an answer that was upvoted at least 5 times"),
    func=lambda user: Post.objects.filter(vote_count__gt=5, author=user, type=Post.ANSWER),
    icon="fa fa-pencil-square-o"
)

STUDENT = AwardDef(
    name=_("Student"),
    desc=_("asked a question with at least 3 up-votes"),
    func=lambda user: Post.objects.filter(vote_count__gt=2, author=user, type=Post.QUESTION),
    icon="fa fa-certificate"
)

TEACHER = AwardDef(
    name=_("Teacher"),
    desc=_("created an answer with at least 3 up-votes"),
    func=lambda user: Post.objects.filter(vote_count__gt=2, author=user, type=Post.ANSWER),
    icon="fa fa-smile-o"
)

COMMENTATOR = AwardDef(
    name=_("Commentator"),
    desc=_("created a comment with at least 3 up-votes"),
    func=lambda user: Post.objects.filter(vote_count__gt=2, author=user, type=Post.COMMENT),
    icon="fa fa-comment"
)

CENTURION = AwardDef(
    name=_("Centurion"),
    desc=_("created 100 posts"),
    func=lambda user: wrap_list(user, Post.objects.filter(author=user).count() > 100),
    icon="fa fa-bolt",
    type=Badge.SILVER,
)

EPIC_QUESTION = AwardDef(
    name=_("Epic Question"),
    desc=_("created a question with more than 10,000 views"),
    func=lambda user: Post.objects.filter(author=user, view_count__gt=10000),
    icon="fa fa-bullseye",
    type=Badge.GOLD,
)

POPULAR = AwardDef(
    name=_("Popular Question"),
    desc=_("created a question with more than 1,000 views"),
    func=lambda user: Post.objects.filter(author=user, view_count__gt=1000),
    icon="fa fa-eye",
    type=Badge.GOLD,
)

ORACLE = AwardDef(
    name=_("Oracle"),
    desc=_("created more than 1,000 posts (questions + answers + comments)"),
    func=lambda user: wrap_list(user, Post.objects.filter(author=user).count() > 1000),
    icon="fa fa-sun-o",
    type=Badge.GOLD,
)

PUNDIT = AwardDef(
    name=_("Pundit"),
    desc=_("created a comment with more than 10 votes"),
    func=lambda user: Post.objects.filter(author=user, type=Post.COMMENT, vote_count__gt=10),
    icon="fa fa-comments-o",
    type=Badge.SILVER,
)

GURU = AwardDef(
    name=_("Guru"),
    desc=_("received more than 100 upvotes"),
    func=lambda user: wrap_list(user, Vote.objects.filter(post__author=user).count() > 100),
    icon="fa fa-beer",
    type=Badge.SILVER,
)

CYLON = AwardDef(
    name=_("Cylon"),
    desc=_("received 1,000 up votes"),
    func=lambda user: wrap_list(user, Vote.objects.filter(post__author=user).count() > 1000),
    icon="fa fa-rocket",
    type=Badge.GOLD,
)

VOTER = AwardDef(
    name=_("Voter"),
    desc=_("voted more than 100 times"),
    func=lambda user: wrap_list(user, Vote.objects.filter(author=user).count() > 100),
    icon="fa fa-thumbs-o-up"
)

SUPPORTER = AwardDef(
    name=_("Supporter"),
    desc=_("voted at least 25 times"),
    func=lambda user: wrap_list(user, Vote.objects.filter(author=user).count() > 25),
    icon="fa fa-thumbs-up",
    type=Badge.SILVER,
)

SCHOLAR = AwardDef(
    name=_("Scholar"),
    desc=_("created an answer that has been accepted"),
    func=lambda user: Post.objects.filter(author=user, type=Post.ANSWER, has_accepted=True),
    icon="fa fa-check-circle-o"
)

PROPHET = AwardDef(
    name=_("Prophet"),
    desc=_("created a post with more than 20 followers"),
    func=lambda user: Post.objects.filter(author=user, type__in=Post.TOP_LEVEL, subs_count__gt=20),
    icon="fa fa-pagelines"
)

LIBRARIAN = AwardDef(
    name=_("Librarian"),
    desc=_("created a post with more than 10 bookmarks"),
    func=lambda user: Post.objects.filter(author=user, type__in=Post.TOP_LEVEL, book_count__gt=10),
    icon="fa fa-bookmark-o"
)

def rising_star(user):
    # The user joined no more than three months ago
    cond = now() < user.profile.date_joined + timedelta(weeks=15)
    cond = cond and Post.objects.filter(author=user).count() > 50
    return wrap_list(user, cond)

RISING_STAR = AwardDef(
    name=_("Rising Star"),
    desc=_("created 50 posts within first three months of joining"),
    func=rising_star,
    icon="fa fa-star",
    type=Badge.GOLD,
)

# These awards can only be earned once
SINGLE_AWARDS = [
    AUTOBIO,
    STUDENT,
    TEACHER,
    COMMENTATOR,
    SUPPORTER,
    SCHOLAR,
    VOTER,
    CENTURION,
    CYLON,
    RISING_STAR,
    GURU,
    POPULAR,
    EPIC_QUESTION,
    ORACLE,
    PUNDIT,
    GOOD_ANSWER,
    GOOD_QUESTION,
    PROPHET,
    LIBRARIAN,
]

GREAT_QUESTION = AwardDef(
    name=_("Great Question"),
    desc=_("created a question with more than 5,000 views"),
    func=lambda user: Post.objects.filter(author=user, view_count__gt=5000),
    icon="fa fa-fire",
    type=Badge.SILVER,
)

GOLD_STANDARD = AwardDef(
    name=_("Gold Standard"),
    desc=_("created a post with more than 25 bookmarks"),
    func=lambda user: Post.objects.filter(author=user, book_count__gt=25),
    icon="fa fa-bookmark",
    type=Badge.GOLD,
)

APPRECIATED = AwardDef(
    name=_("Appreciated"),
    desc=_("created a post with more than 5 votes"),
    func=lambda user: Post.objects.filter(author=user, vote_count__gt=4),
    icon="fa fa-heart",
    type=Badge.SILVER,
)


# These awards can be won multiple times
MULTI_AWARDS = [
    GREAT_QUESTION,
    GOLD_STANDARD,
    APPRECIATED,
]

ALL_AWARDS = SINGLE_AWARDS + MULTI_AWARDS