#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py loaddata fill_db.json

psql "$POSTGRESQL_URL" -f ./count_unique_words.sql
psql "$POSTGRESQL_URL" -f ./count_words.sql
