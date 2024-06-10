[![flake8 Lint](https://github.com/acdh-oeaw/cbab/actions/workflows/lint.yml/badge.svg)](https://github.com/acdh-oeaw/cbab/actions/workflows/lint.yml)
[![Test](https://github.com/acdh-oeaw/cbab/actions/workflows/test.yml/badge.svg)](https://acdh-oeaw.github.io/cbab/)
[![workflows starter](https://github.com/acdh-oeaw/cbab/actions/workflows/starter.yaml/badge.svg)](https://github.com/acdh-oeaw/cbab/actions/workflows/starter.yaml)

# About

The CBAB (Cremation Bronze Age Burials) application is used for coordinated assessment of the cremation burials in the Late Bronze Age (14th – 9th century BC) based on a shared database.

It is a Django based web application written in Python 3 and developed at the Austrian Centre for Digital Humanities and Cultural Heritage (ACDH-CH).

For more information about the project please visit https://www.oeaw.ac.at/acdh/projects/cbab/

# Licensing

All code unless otherwise noted is licensed under the terms of the MIT License (MIT).
Please refer to the file COPYING in the root directory of this repository.

# Installation

* Clone this repository.
* create a virtual env and install needed packages, e.g. by running
  * `python -m venv venv`
  * `source venv/bin/activate`
  * and `pip install -r requirements.text`
* copy and adatpt `env.env` to `env.secret` and run (adapted) `set_env_varibales.sh` (or choose any other method you like to set environment variables)
* start the dev-server `python manage.py runserver` (run migrations if needed)

## Docker

At the ACDH-CH we use a centralized database-server. So instead of spawning a database for each service our services are talking to a database on this centralized db-server. This setup is reflected in the dockerized setting as well, meaning it expects an already existing database (either on your host, e.g. accessible via 'localhost' or some remote one)

### building the image

* `docker build -t cbab:latest .`
* `docker build -t cbab:latest --no-cache .`


### running the image

To run the image you should provide an `.env` file to pass in needed environment variables; see example below:

* `docker run -it -p 8020:8020 --rm --env-file docker.env --name cbab cbab:latest`