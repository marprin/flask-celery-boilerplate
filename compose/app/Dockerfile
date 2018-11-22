FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
STOPSIGNAL SIGTERM

RUN apk update && apk upgrade

RUN apk add gcc --no-cache

RUN apk add --virtual build-deps postgresql-dev gcc musl-dev --update-cache --no-cache

WORKDIR /app

COPY ./requirements /requirements

RUN pip install pip --upgrade && pip install -r /requirements/prod.txt --no-cache-dir

ADD . /app

CMD gunicorn -b 0.0.0.0:9300 -t 30 --graceful-timeout 60 wsgi:app -p /tmp/gunicorn.pid
