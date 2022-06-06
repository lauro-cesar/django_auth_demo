#!/bin/bash
echo "Starting Django"

timeout=0
isReady=0
python3 -m venv .venv 
source .venv/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt

if [ -z ${DATABASE_PORT} ] ; then
    until nc -z ${DATABASE_HOST} ${DATABASE_PORT}; do
    echo "$(date) - waiting for database"
    sleep 5
done
fi


python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput

screen -wipe

screen -dmS queue celery -b redis://$REDIS_HOST:$REDIS_PORT/$REDIS_DB -A project worker -B -E -Q $REDIS_QUEUE_NAME

screen -dmS django gunicorn project.wsgi:application --bind 0.0.0.0:8001 --proxy-protocol --strip-header-spaces --graceful-timeout=900 --timeout=900

echo "Django Started"

touch /tmp/log.txt

tail -f /tmp/log.txt

exec "$@"
