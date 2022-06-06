import os
import sys


ENV_API = """
DEBUG=1
LOCAL=0
SECRET_KEY='_'
FQDNS="localhost,127.0.0.1"
DJANGO_HOST=django_project
DJANGO_PORT=8001
SENDGRID_API_KEY=""
DEFAULT_FROM_EMAIL="naoresponda@"
"""


ENV_COMMON = """
TZ="America/Sao_Paulo"
PRIVATE_DIR="/media/private/"
"""

ENV_REDIS="""
REDIS_HOST=django_redis
REDIS_PORT=6379
REDIS_QUEUE_NAME=project_redis
REDIS_DB=1
"""

ENV_MEMCACHE="""
memcache
CACHE_HOST=django_cache
"""

ENV_NGINX="""
nginx
STATIC_DIR="/home/django_project/static/"
MEDIA_DIR="/home/django_project/media/"
"""

ENV_DB="""
DATABASE_HOST=django_db
DATABASE_PORT=5432
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_TYPE=pg
DATABASE_USER=db_user
DATABASE_PASSWORD=pass
DATABASE_NAME=db_name
POSTGRES_PASSWORD=pass
POSTGRES_USER=db_user
POSTGRES_DB=db_name
"""



ENV_PROJECT="""
PROJECT_DIR=django_project
DOCKER_PROJECT_DIR=django_docker
DOCKER_NAME=project_name
DJANGO_SERVICE_NAME=django_project
"""

destinos =[
    '.env-project.yaml',
    '.env-db.yaml',
    '.env-api.yaml',
    '.env-common.yaml',
    '.env-redis.yaml',
    '.env-memcache.yaml',
    '.env-nginx.yaml']
    


for f in destinos:
    with open(f,"w") as d:
        d.write("\n")
