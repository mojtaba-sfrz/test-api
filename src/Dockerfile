# pull official base image
FROM python:3.11.0-alpine

# set work directory
WORKDIR C:/Users/mojtaba/projects/fastapi-crud/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt C:/Users/mojtaba/projects/fastapi-crud/src/app/requirements.txt

# install dependencies
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
         openssl-dev libffi-dev gcc musl-dev python3-dev \
         postgresql-dev bash \

    && pip install --upgrade pip setuptools wheel \
    && pip install -r C:/Users/mojtaba/projects/fastapi-crud/src/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . C:/Users/mojtaba/projects/fastapi-crud/src/app