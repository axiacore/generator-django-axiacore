#!/bin/bash
. ../bin/activate

curl -fsSL https://raw.githubusercontent.com/AxiaCore/axiacore_utils/master/scripts/update_requirements.sh | bash

./manage.py collectstatic --noinput

./manage.py migrate --noinput
./manage.py clear_cache

touch app/local_settings.py
