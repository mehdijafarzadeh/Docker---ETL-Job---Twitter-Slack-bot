# Docker Pipeline - ETL Job - Twitter, Slack APIs 

## Table of Contents
- [General info](#general)
- [Needed Libraries](#Needed_libraries)
- [Setup](#setup)
- [Commands](#Some_Useful_Docker_Commands)

### General
In this very simple Project, I've started to build a docker-compose to collect twitts from twitter API and transform it into wished Information to post an Slack.
It contains  of tweet collector, sentiment analysis and posting them via slack bot.  

Followings applied:
- Docker Image, Container, Compose
- Twitter API
- Slack API
- Logging
- .env -> key protection

### Needed Libraries
- Python 3.8
- tweepy
- vaderSentiment
- sqlalchemy
- dotenv
- requests
- pandas
- logging

### Setup
To start with Twitt Collector you need Twitter Developer Account to get `API KEY`, `API SECRET` and `access token`, `access token secret`.  
You can make a new account on twitter dev-acc [here](https://developer.twitter.com/en/apply).  

* note: Do not forget to put your Credential into .env file and aslo do not forget to put .env in the list of .gitignore


### Some Useful Docker Commands 

For running these commands you need to `cd` into the folder that contains the `docker-compose.yml` file.

#### (re-)build images of services 

```
docker-compose build
```
#### run/start containers in the background

```
docker-compose up -d
```

#### list all running containers/ services

```
docker-compose ps
```

#### view the output of individual services

```
docker-compose logs <servicename>
```

#### Open a bash shell inside a disposible container 

The container will be removed after exiting the container

```
docker-compose run --rm my_first_service bash
```

#### list running containers

```
docker container ls
```

#### list running and stopped containers

```
docker container ls --all
```

#### start a new fresh container (based on the `ubuntu` image)

```
docker run -d -it --name my_container ubuntu
```
with volume mapping:
```
docker run -d -it --name my_container -v $PWD/src:/app ubuntu
```
with port mapping:
```
docker run -d -it --name my_container -p 5555:5432 ubuntu
```

#### attach to the main process on a running container

```
docker attach my_container
```

#### create a new process on the container

a bash shell:
```
docker exec -it my_container bash
```

psql:
```
docker exec -it my_container psql -U postgres -p 5432
```

#### start and stop containers

```
docker stop my_container
docker start my_container
```

#### list your downloaded images

```
docker image ls
```

#### build an image from a dockerfile

```
docker build -t my_image ./my_first_imag
```

