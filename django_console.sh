echo "Run Docker Django bash"

source variables.sh
sudo  docker compose -p $DOCKER_NAME exec django_project bash
