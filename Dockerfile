FROM python:3.6-slim

# Copy in your requirements file:
ADD requirements.txt /requirements.txt

# Install all build deps:
RUN set -ex \
    && apt-get update \
    && apt-get install -y \
        gcc \
        gettext \
        git \
        mysql-client \
        libmysqlclient-dev \
        postgresql-client \
        libpq-dev \
        libjpeg62 \
        libjpeg62-turbo-dev \
    && pip install --no-cache-dir -r /requirements.txt

# Copy the application code to the container:
RUN mkdir /code/
WORKDIR /code/
ADD . /code/

# uWSGI will listen on this port:
EXPOSE 8000

# Add any custom, static environment variables needed by Django:
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=app.settings \
    ALLOWED_HOSTS=* \
    RDS_HOSTNAME=db \
    RDS_PORT=5432 \
    RDS_DB_NAME=postgres \
    RDS_USERNAME=postgres \
    RDS_PASSWORD=password \
    EMAIL_HOST=mail \
    EMAIL_PORT=1025 \
    EMAIL_HOST_USER=user \
    EMAIL_HOST_PASSWORD=password

# uWSGI configuration:
ENV UWSGI_WSGI_FILE=app/wsgi.py \
    UWSGI_HTTP=:8000 \
    UWSGI_MASTER=1 \
    UWSGI_WORKERS=2 \
    UWSGI_THREADS=8 \
    UWSGI_UID=1000 \
    UWSGI_GID=2000 \
    UWSGI_LAZY_APPS=1 \
    UWSGI_WSGI_ENV_BEHAVIOR=holy

# Docker entrypoint:
ENV DJANGO_MANAGEPY_MIGRATE=on \
    DJANGO_MANAGEPY_COLLECTSTATIC=on \
    DJANGO_MANAGEPY_UPDATEINDEX=on
ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start uWSGI:
CMD ["uwsgi", "--http-auto-chunked", "--http-keepalive"]