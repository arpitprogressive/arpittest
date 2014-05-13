#!/usr/bin/env bash

# Change to pursuite user
source /opt/pursuite/bin/activate
cd /opt/pursuite/django-pursuite

# Fetch the latest code
git fetch origin
git checkout origin/master

python setup.py install
python manage.py collectstatic --noinput --settings=pursuite.settings.production 
