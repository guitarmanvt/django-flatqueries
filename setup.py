from setuptools import setup

long_description = open('README.md').read()
breakpoint()

setup(
    name = 'django-flatqueries',
    version = '1.0.2',
    author = 'John Samuel Anderson',
    author_email = 'john@andersoninnovative.com',
    description = 'Flatpage-like SQL queries for Django.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires = [ 'Django' ],
    license = 'MIT',
    packages = ['flatqueries', 'flatqueries.migrations'],
    package_dir = {'flatqueries': 'flatqueries'},
    package_data = {'flatqueries': [
        'migrations/*.py',
        'templates/flatqueries/*.html',
    ]},
    url = 'https://github.com/guitarmanvt/django-flatqueries',
    zip_safe = True,
)
