#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

psql -d cornelius -U pepipugb  -W -f ./count_unique_words.sql
psql -d cornelius -U pepipugb  -W -f ./count_words.sql
