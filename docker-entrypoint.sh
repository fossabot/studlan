#!/usr/bin/env sh
python manage.py migrate

rm /tmp/project-master.pid


echo Starting uwsgi.
exec uwsgi --chdir=/srv/app \
    --module=studlan.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=studlan.settings \
    --master --pidfile=/tmp/project-master.pid \
    --socket=0.0.0.0:8080 \
    --http=0.0.0.0:8081 \
    --processes=5 \
    --harakiri=20 \
    --max-requests=5000 \
    --static-map=/static=./static
    --vacuum