#!/usr/bin/env bash
# exit on error
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt #la lista de requisitos necesarios para que funncione la API

python manage.py collectstatic --no-input
python manage.py migrate