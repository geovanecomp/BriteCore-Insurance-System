#!/bin/bash

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Loading field types fixtures..."
python manage.py loaddata field_types/fixtures/field_types.json

echo "==> Done!"
