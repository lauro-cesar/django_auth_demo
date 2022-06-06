#!/bin/bash
source variables.sh

echo "Build Docker"

sudo docker compose -p $DOCKER_NAME down -v
sudo docker compose -p $DOCKER_NAME build
sudo docker compose -p $DOCKER_NAME up -d
