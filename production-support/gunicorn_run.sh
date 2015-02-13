#!/bin/bash

set -e 

export HOME=/usr/local/apps/geosurvey/server
export VENV=/usr/local/venv/geosurvey
PROJECT=geosurvey
BIND=127.0.0.1:8888
GUNICORN=$VENV/bin/gunicorn
LOGFILE=/var/log/nginx/geosurvey.log
TIMEOUT_S=3000
NUM_WORKERS=5
USER=nginx
GROUP=deploy

cd $HOME
source $VENV/bin/activate
exec $GUNICORN wsgi:application \
     --bind $BIND \
     --workers $NUM_WORKERS \
     --timeout $TIMEOUT_S \
     --user=$USER --group=$GROUP --log-level=DEBUG --log-file=$LOGFILE 2>>$LOGFILE &

