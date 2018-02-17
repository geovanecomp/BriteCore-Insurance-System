#!/bin/bash

echo "==> Removing all data from the database..."
python manage.py flush --noinput

echo "==> Starting database population!"

echo "==> Loading field types fixtures..."
python manage.py loaddata field_types/fixtures/field_types.json

echo "==> Loading fields fixtures..."
python manage.py loaddata fields/fixtures/fields.json

echo "==> Loading risk types fixtures..."
python manage.py loaddata risk_types/fixtures/risk_types.json

echo "==> Loading risks fixtures..."
python manage.py loaddata risks/fixtures/risks.json

echo "==> Loading fields by risk fixtures..."
python manage.py loaddata fields_by_risk/fixtures/fields_by_risk.json

echo "==> Done!"
