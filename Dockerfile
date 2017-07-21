FROM        python:3.6

WORKDIR     /var/app

RUN apt-get update && apt-get install -y \
        postgresql-client \
        libpq-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/

COPY        requirements.txt /var/app
COPY        test-requirements.txt /var/app

RUN         pip install --no-cache-dir -r /var/app/test-requirements.txt