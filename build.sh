#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

psql "$POSTGRESQL_URL" -v owner="$POSTGRES_USER" -f ./count_unique_words.sql