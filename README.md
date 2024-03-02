# Speech-to-Text Backend


## Application Features

A speech-to-text user account creation with a voice-over welcome message. (Backend Code)

### Features
- A User can register ```domain/api/v1/register/```
- A User can login ```domain/api/v1/login/```
- A User can retrieve his/her detail ```domain/api/v1/account/```
- A User can logout ```domain/api/v1/logout/```

**NB:** You have to add the authorization token to the header of your request in order to access *retrieve* and *logout* endpoints e.g `Authorization: Token 94e052d826593f57118aa5c49b4d7b1786c37b6d`

## Technologies

### Backend

- [Python](https://www.python.org/) is a programming language that lets you work more quickly and integrate your systems more effectively.
- [Django](https://www.djangoproject.com/) makes it easier to build better web apps more quickly and with less code.
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.
- [PostgreSQL](https://www.postgresql.org/) A powerful, open source object-relational database system.
- [Docker](https://www.docker.com/) is a platform designed to help developers build, share, and run container applications.


## Installation

- Install [Python](https://www.python.org/), [PostgreSQL](https://www.postgresql.org/) and [Docker](https://www.docker.com/) on your computer
- Clone this repository ```git clone https://github.com/nouwatinjacob/dukka-test.git```
- Navigate to the directoty ```cd dukka-test```
- add a ```.env``` file to the root of the project with neccessary environment added by following the example in .env.sample file
- To start the app by running ```docker-compose up -d --build```

## Testing

- Create a test database of your choice by following the example in .env.sample file
- Run test with `python manage.py test`


## API host

- The backend application is hosted on render platform. You can always visit it via this link [https://dukka-zszl.onrender.com](https://dukka-zszl.onrender.com)  

