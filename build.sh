#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install -r requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('theadmin@example.com', 'password'); print(User.objects.all())" | python manage.py shell

