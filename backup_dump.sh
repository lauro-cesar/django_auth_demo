#!/bin/bash
source variables.sh
sudo docker compose -p $DOCKER_NAME exec django_project python manage.py dumpdata  --natural-foreign --natural-primary -e contenttypes -e admin -e auth.Permission -e authtoken --indent 4 > bk_$(date +%Y_%m_%d_%H_%M_%s).json
