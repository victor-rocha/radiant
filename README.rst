
Radiant
========================

Below you will find basic setup and deployment instructions for the radiant
project. To begin you should have the following applications installed on your
local development system:

- Python >= 3.4
- `pip <http://www.pip-installer.org/>`_ >= 1.5
- `virtualenv <http://www.virtualenv.org/>`_ >= 1.10
- `virtualenvwrapper <http://pypi.python.org/pypi/virtualenvwrapper>`_ >= 3.0
- Postgres >= 9.3
- git >= 1.7


Getting Started
------------------------

First clone the repository from Github and switch to the new directory::

    $ git clone git@github.com:[ORGANIZATION]/radiant.git
    $ cd radiant

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    # Check that you have python3.4 installed
    $ which python3.4
    $ mkvirtualenv radiant -p `which python3.4`
    (radiant)$ $VIRTUAL_ENV/bin/pip install -r $PWD/requirements/dev.txt

Next, we'll set up our local environment variables. We use `django-dotenv
<https://github.com/jpadilla/django-dotenv>`_ to help with this. It reads environment variables
located in a file name ``.env`` in the top level directory of the project. The only variable we need
to start is ``DJANGO_SETTINGS_MODULE``::

    (radiant)$ cp radiant/settings/local.example.py radiant/settings/local.py
    (radiant)$ echo "DJANGO_SETTINGS_MODULE=radiant.settings.local" > .env

Create the Postgres database and run the initial migrate::

    (radiant)$ createdb -E UTF-8 radiant
    (radiant)$ python manage.py migrate

You should now be able to run the development server::

    (radiant)$ python manage.py runserver


Deployment
------------------------

The deployment of requires Fabric but Fabric does not yet support Python 3. You
must either create a new virtualenv for the deployment::

    # Create a new virtualenv for the deployment
    $ mkvirtualenv radiant-deploy -p `which python2.7`
    (radiant-deploy)$ pip install -r requirements/deploy.txt

or install the deploy requirements
globally::

    $ sudo pip install -r requirements/deploy.txt


You can deploy changes to a particular environment with
the ``deploy`` command::

    $ fab staging deploy

New requirements or migrations are detected by parsing the VCS changes and
will be installed/run automatically.
