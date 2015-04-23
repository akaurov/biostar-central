#!/bin/bash
set -ue

# This is required so that the default configuration file works.
source /var/www/tetrad/live/deploy.env

# Location of the log file
LOGFILE=/var/www/tetrad/live/logs/celery-beat.log

# The name of the application.
APP="biostar"

# The gunicorn instance to run.
CELERY="/var/envs/tetrad/bin/celery"

echo "starting celery beat with DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"

$CELERY -A $APP beat -l info -f $LOGFILE

