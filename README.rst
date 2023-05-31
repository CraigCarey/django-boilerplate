Django Boilerplate
==================

Features:
 * Uses django-split-settings to enable separation of settings
 * Settings are overridable from the command line
 * Linting & pre-commit
 * Apps totally isolated from project
 * Basic user registration app using crispy forms + bootstrap5

Project Setup
=============

Install dependencies:

.. code-block::

    apt install libpq-dev
    pip install poetry
    poetry install


Create your own version of settings:

.. code-block::

    mkdir -p local
    cp core/project/settings/templates/settings.dev.py local
    cp core/project/settings/templates/settings.unittests.py local

Use local dev settings:

.. code-block::

    CORESETTINGS_LOCAL_SETTINGS_PATH=/path/to/file make run-server

When running in docker:

.. code-block::

    CORESETTINGS_IN_DOCKER=true make run-server

SMTP Setup
==========
Without the following environment variables emails will be written to a local file.

.. code-block::
    export CORESETTINGS_HOST_EMAIL_ADDRESS="<insert email address>"
    export CORESETTINGS_HOST_EMAIL_PASSWORD="<insert password>"


Containers
==========

This runs the db service only, for local development

.. code-block::
    make make dev-docker-compose-up


To run the app in prod:

.. code-block::
    make make prod-docker-compose-up


Overriding DB Config
====================

`CORESETTINGS_DATABASES` env var takes precedence:

.. code-block::
    CORESETTINGS_DATABASES='{"default":{"HOST":"db"}}' make run-server

After that, `DB_MODE` env var:

.. code-block::
    CORESETTINGS_DB_MODE=postgres make run-server

If neither env vars are provided, it will default to sqlite

TODO
====
 * prod server (Daphne?)
