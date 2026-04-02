# django-flatqueries

## Installing the app package from PyPI

If you already have a working Django 4+ project and you just want to install the app:

1. Get the package:
    pip install django-flatqueries

2. Add 'flatqueries' to your `INSTALLED_APPS` in settings.py.

3. Add this to your urls.py:

    path("flatqueries/", include("flatqueries.urls"))

4. Create the database table required by this app:

    python manage.py migrate

5. Make sure you have a template that can be resolved as `base.html` and
   contains a `content` block.

## Getting the sample project

This project runs out-of-the box on Django 4.2.17 (Python 3.8.10 and 3.12.3).

1. Grab the code.
    git clone https://github.com/guitarmanvt/django-flatqueries demo
2. cd demo/sample
3. Create the database and a superuser.
    python manage.py migrate
    python manage.py createsuperuser
4. Load the demo data. \*(Optional, but see deployment note)
    python manage.py loaddata demo_data.json
5. Start the local development server.
    python manage.py runserver
6. Login at http://127.0.0.1:8000/admin to play with flatqueries.


## Usage

### TO RUN A FLATQUERY

1. On its view page, click the "view on site" button.
2. Click the "Run" button.

### DEPLOYMENT: VERY IMPORTANT

If you put this on another domain, you need to make sure your "site" values
are correct. Otherwise, the "view on site" button will not work correctly!

### SECURITY

For editing, the standard Django Admin permissions apply. Any superuser will
be able to edit, as well as any staff person with the appropriate permissions.

For running queries, an additional permission is needed for staff users.
Assign `flatqueries.can_run_query` to grant this permission to users or groups.

Still, be careful not to let query URLs fall into the hands of users you
don't want running them. If you ignore this warning, then any trouble that
results is YOUR OWN FAULT. :P

## Changelog

### 1.0.1

* Added changelog
* Included (missing) migrations in package
