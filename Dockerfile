FROM python:3.7-alpine
MAINTAINER David Glaser

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# update postrges client on alpine
RUN apk add --update --no-cache postgresql-client

# install temp files to install requirements.txt that will be removed after install
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
