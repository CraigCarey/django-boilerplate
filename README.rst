Django Boilerplate
==================

Based on `New Boston YouTube tutorials <https://youtu.be/DaxcmbWcdTA>`_

Features:
 * Uses django-split-settings to enable separation of settings
 * Settings are overridable from the command line
 * Linting & pre-commit

Project Setup
=============

Install dependencies:

.. code-block::

    apt install libpq-dev
    poetry install


Create your own version of settings:

.. code-block::

    mkdir -p local
    cp core/project/settings/templates/settings.dev.py local

Use local dev settings:

.. code-block::

    CORESETTINGS_LOCAL_SETTINGS_PATH=/path/to/file make run-server

When running in docker:

.. code-block::

    CORESETTINGS_IN_DOCKER=true make run-server
