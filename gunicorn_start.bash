#!/bin/bash
source "/home/ubuntu/backend/environement.txt"
NAME="backend"               					                  # Name of the application
DJANGODIR=/home/ubuntu/backend             				                  # Django project directory
DJANGOENVDIR=/home/ubuntu/venv            			                    # Django project env
SOCKFILE=/home/ubuntu/venv/run/gunicorn.sock  		                  # we will communicte using this unix socket
USER=ubuntu                   				                  # the user to run as
GROUP=ubuntu                  					                # the group to run as
NUM_WORKERS=3                                    				# how many worker processes should Gunicorn spawn (2 * CPUs + 1)
DJANGO_SETTINGS_MODULE=backend.settings.production
if [ $environement = "preproduction" ]
then
  DJANGO_SETTINGS_MODULE=backend.settings.preproduction # which settings file should Django use
else [ $environement = "production" ]
  DJANGO_SETTINGS_MODULE=backend.settings.production
fi
DJANGO_WSGI_MODULE=backend.wsgi                     						            # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGOENVDIR
source bin/activate
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ${DJANGOENVDIR}/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-