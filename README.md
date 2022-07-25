# Twitter_Backend_Clone
A simple rest api with jwt token authentication to be used as a backend for a simple twitter clone.

## Features
- Tweets
- Messages
- Comments ( these are not threaded as I am using a relational database which is not well suited towards threaded comments )
- JWT Authentication

## How To Run

- This app is containerised so it is really easy to get up and running.

### Development

- 1) Modify the .env.dev and .env.db files and change the POSTGRES_USER, POSTGRES_PASSWORD and the SECRET_KEY to your preferences
- 2) Open a terminal and execute this command `docker-compose -f docker-compose-dev.yml up --build`
- 3) Open a terminal and excute this command `docker-compose -f docker-compose-dev.yml run web python manage.py migrate`
- 4) Open a terminal and execute this command `docker-compose -f docker-compose-dev.yml up`

### Production

This setup is not ideal and I would instead suggest follow your preferred cloud providers guide on hosting a django project.

- 1) Modify the .env.dev and .env.db files and change the POSTGRES_USER, POSTGRES_PASSWORD and the SECRET_KEY to your preferences
- 2) Open a terminal and execute this command `docker-compose -f docker-compose-prod.yml up --build`
- 3) Open a terminal and excute this command `docker-compose -f docker-compose-prod.yml run web python manage.py migrate`
- 4) Open a terminal and execute this command `docker-compose -f docker-compose-prod.yml up`

### Database
- If you would like to you can use your own postgres database instead of the included docker one in order to do this you just need to remove the db app from the docker-compose file and modify the POSTGRES_HOST, POSTGRES_USER and POSTGRES_PASSWORD enviroment variables