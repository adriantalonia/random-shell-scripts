# Docker commands

### See docker resources
```sh
# See docker images
docker images
docker images ls

# See active docker contianers
docker ps
# See all docker container
docker ps -a
# Filter docker image
docker ps -a | grep my-image

# See docker networks
docker network ls
```

### Pull a docker image
```sh
docker pull [docker-image]
```

### Run docker image in a container
```sh
# To run an image with a continer name
docker run [docker-image] --name my-docker-contianer

# To run it in de-attached mode
docker run -d [docker-image]

# To bind a port
docker run -p 5001:5000 [docker-image]

# To pass environment variables
docker run -r MY_PASS=mypassword [docker-image]

# To specify the network
docker run --net my-network [docker-image]

# MongoDB example with all parameters
docker run -d \
-p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=admin \
-e MONGO_INITDB_ROOT_PASSWORD=password \
--name mongodb \
--net mongo-network \
mongo
```

### Stop docker contianer
```sh
docker stop [docker-container-id]
```

### Enter into a docker container
```sh
# -it stands for interactive terminal
docker exec -it [docker-container-id] /bin/bash
```

### Crete / list / delete a docker network
```sh
docker network create [netowrk-name]

docker netowrk ls

docker network rm [docker-network-id]
```

### Get the logs
```sh
docker logs [docker-contianer-id]

# Get the last part of the logs
docker logs [docker-contianer-id] | tail

# Stream the logs
docker logs [docker-contianer-id] -f
```

### Run mongo-express container
```sh
docker run -d \
-p 8081:8081 \
-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
-e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
--net mongo-network \
--name mongo-express \
-e ME_CONFIG_MONGODB_SERVER=mongodb \
mongo-express
```

### Start / stop containers with docker-compose

[See docker-compose-example.yaml file for reference](./docker-compose-example.yaml)

```sh
docker-compose -f my-docker-compose-file.yaml up

# Run it in de-attached mode
docker-compose -d -f my-docker-compose-file.yaml up

docker-compose -f my-docker-compose-file.yaml down
```

### Worj with Docker images
```sh
#Build docker image
docker build -t my-app:1.0 .

# Check docker image
docker images # -> my-app 1.0 88ddf1a96c75 5 seconds ago 121MB

# Delete docker container
docker rm [container-id]

# Delete docker image
docker rmi [docker-image]
```

### Tag and push Docker image
```sh
docker tag my-image:1.0 my-registry/my-image:1.0

docker push my-registry/my-image:1.0
```

