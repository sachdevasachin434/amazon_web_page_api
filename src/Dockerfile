FROM python:3.6.9-alpine3.9

LABEL MAINTAINER="Sachin Sachdeva <sachdevasachin434@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

COPY . /var/www/
RUN pip install -r requirements.txt

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "python", "main.py"]
# TODO: Setup gunicorn in production
