#!/bin/bash
git add .
# git reset push.sh
git commit -m "modificaciones en casa"
git push heroku master

# heroku run python manage.py migrate --settings=config.settings_heroku
# heroku run python manage.py createsuperuser --settings=config.settings_heroku
# heroku run python manage.py makemigrations --settings=config.settings_heroku
# heroku run python manage.py migrate --settings=config.settings_heroku
