
# pull official base image
FROM python:3.9
RUN apt-get update && apt-get -y install apt-utils postgresql-client binutils libgdal-dev libproj-dev gdal-bin postgis netcat screen

RUN export LC_ALL="pt_BR.UTF-8"
RUN export LC_CTYPE="pt_BR.UTF-8"

ENV APP_HOME=/home/django_project
RUN mkdir -p $APP_HOME
RUN useradd -U -M -d $APP_HOME app
WORKDIR $APP_HOME
USER app