# About

The CBAB (Cremation Bronze Age Burials) application is used for coordinated assessment of the cremation burials in the Late Bronze Age (14th – 9th century BC) based on a shared database.

It is a Django based web application written in Python 3 and developed at the Austrian Centre for Digital Humanities (ACDH).

For more information about the project please visit https://www.oeaw.ac.at/acdh/projects/cbab/

# Licensing

All code unless otherwise noted is licensed under the terms of the MIT License (MIT).
Please refer to the file COPYING in the root directory of this repository.

# Installation

Clone this repository.
Adapt the setting files in cbab/settings/.

Install the required packages:

    pip install requirements/requirements.txt

Make the database migrations:

    python manage.py makemigrations
    python manage.py migrate

# Tests

To use the tests install the required packages:

    pip install requirements/requirements_test.txt

To run tests with HTML coverage report execute:

    python manage.py test --settings=cbab.settings.test

The HTML reports will be available at: cover/index.html
