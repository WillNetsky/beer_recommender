#!/bin/bash

NAME="Punctuations-App"
APPDIR=/home/ubuntu/projects/iris/app
SOCKFILE=/home/ubuntu/www/sock
NUM_WORKERS=3

echo "Starting $NAME"

# activate the virtualenv
source activate env

export PYTHONPATH=$APPDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your unicorn
exec gunicorn run:application -b 0.0.0.0:9000 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --bind=unix:$SOCKFILE