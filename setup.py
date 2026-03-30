from setuptools import setup

setup(
    name = 'django-flatqueries',
    version = '1.0.0',
    author = 'John Samuel Anderson',
    author_email = 'john@andersoninnovative.com',
    description = 'Flatpage-like SQL queries for Django.',
    long_description=open('README.md').read(),
    install_requires = [ 'Django' ],
    license = 'MIT',
    packages = ['flatqueries'],
    package_dir = {'flatqueries': 'flatqueries'},
    package_data = {'flatqueries': ['templates/flatqueries/*.html']},
    url = 'https://github.com/guitarmanvt/django-flatqueries',
    zip_safe = True,
)
