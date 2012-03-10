This project runs out-of-the box on Django 1.3. Here's how:

1. Grab the code.
2. cd /path/to/sample_project
3. python manage.py syncdb  
    - Yes, create a superuser
4. python manage.py runserver
5. Login at http://127.0.0.1:8000/admin to play with flatqueries.

TO RUN A FLATQUERY:
1. On its view page, click the "view on site" button.
2. Click the "Run" button.

DEPLOYMENT: VERY IMPORTANT
If you put this on another domain, you need to make sure your "site" values
are correct. Otherwise, the "view on site" button will not work correctly!

SECURITY
Basically, there is none, beyond requiring login. So, be careful not to let
query URLs fall into the hands of users you don't want running them. If you
ignore this warning, then any trouble that results is YOUR OWN FAULT. :P

