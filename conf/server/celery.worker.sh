#!/bin/bash
set -ue

# This is required so that the default configuration file works.
source /var/www/tetrad/live/deploy.env

# Location of the log file
LOGFILE=/var/www/tetrad/live/logs/%n-%i.log

# The concurrency level
NUM_WORKERS=2

# How many tasks per child process
MAX_TASK=1000

# The name of the application.
APP="biostar"

# The logging level
LOGLEVEL=info

# The gunicorn instance to run.
CELERY="/var/envs/tetrad/bin/celery"

echo "starting celery worker with DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"

exec $CELERY -A $APP worker -l info --maxtasksperchild $MAX_TASK --concurrency $NUM_WORKERS -f $LOGFILE

