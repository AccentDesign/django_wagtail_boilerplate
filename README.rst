**************************
Django Wagtail Boilerplate
**************************

|Build_Status| |Coverage_Status|

.. |Build_Status| image:: https://circleci.com/gh/AccentDesign/django_wagtail_boilerplate.svg?style=svg
   :target: https://circleci.com/gh/AccentDesign/django_wagtail_boilerplate
.. |Coverage_Status| image:: http://img.shields.io/coveralls/AccentDesign/django_wagtail_boilerplate/master.svg
   :target: https://coveralls.io/r/AccentDesign/django_wagtail_boilerplate?branch=master

Description
***********

Bare bones starter project complete with the following

- Email authentication
- Karma CSS
- Wagtail
- Postgres
- Postgres Search Backend

Getting Started
***************

1, Clone the repo::

    git clone https://github.com/AccentDesign/django_wagtail_boilerplate.git


2, Docker & Python

Build the container::

    docker-compose build

Up the container, this will also run migrations for you::

    docker-compose up

Create yourself a superuser::

    docker-compose exec app bash
    python manage.py createsuperuser --email=admin@example.com --first_name=Admin --last_name=User


Run python migrations manually::

    docker-compose exec app bash
    python manage.py migrate


Load the initial homepage data::

    docker-compose exec app bash
    python manage.py loaddata initial

Ready!!
*******

The container is ready at http://<docker host ip>:8000/ and a mail server ready at http://<docker host ip>:1080/


Testing
*******

To see the test results and coverage report run::

   docker-compose exec app bash
   make test

The html coverage report is visible in the browser by looking at the htmlcov/index.html once the tests have run.


Styling
*******

1, You will need node js installed, please see online for setup

2, To make any style tweaks you will need to install all project dependencies like so::

    npm install

3, Download the fontello icons, the config file is in ``static/scss/fontello/config.json``::

    npm run fontello-install

4, Build and watch the scss::

    npm run watch-css
