==================
django-flatqueries
==================

Installing the app package from PyPI
====================================
If you already have a working Django 1.3+ project and you just want to install the app:

1. Get the package:
    pip install django-flatqueries

2. Add 'flatqueries' to your INSTALLED_APPS in settings.py.

3. Add this to your urls.py:

    (r'^flatqueries/', 'flatqueries.urls')

4. Create the database table required by this app:

    python manage.py syncdb

Getting the sample project
==========================
This project runs out-of-the box on Django 1.3. Here's how:

1. Grab the code.
    svn checkout http://django-flatqueries.googlecode.com/svn/trunk django-flatqueries-demo
2. cd django-flatqueries-demo/sample_project
3. Create the database.
    python manage.py syncdb
    - Yes, create a superuser
4. Load the demo data. \*(Optional, but see deployment note)
    python manage.py loaddata demo_data.json
5. Start the local development server.
    python manage.py runserver
6. Login at http://127.0.0.1:8000/admin to play with flatqueries.


Usage
=====

TO RUN A FLATQUERY
------------------
1. On its view page, click the "view on site" button.
2. Click the "Run" button.

DEPLOYMENT: VERY IMPORTANT
--------------------------
If you put this on another domain, you need to make sure your "site" values
are correct. Otherwise, the "view on site" button will not work correctly!

SECURITY
--------
For editing, the standard Django Admin permissions apply. Any superuser will
be able to edit, as well as any staff person with the appropriate permissions.

For running queries, an additional permission is needed for staff users.
Assign 'flatqueries.can_run_query' to grant this permission to users or groups.

Still, be careful not to let query URLs fall into the hands of users you
don't want running them. If you ignore this warning, then any trouble that
results is YOUR OWN FAULT. :P
