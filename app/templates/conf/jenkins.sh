#!/bin/bash

. ../bin/activate

curl -fsSL https://gist.github.com/camilonova/5556473/raw/update_requirements.sh | bash

./manage.py syncdb --noinput
./manage.py migrate --no-initial-data --noinput
compass compile app/media/

touch app/local_settings.py

curl -fsSL https://gist.github.com/camilonova/5556746/raw/jshint_report.sh | bash
curl -fsSL https://gist.github.com/camilonova/5556741/raw/cloc_report.sh | bash
./manage.py collectstatic --ignore=uploads --noinput
./manage.py jenkins

curl --data "job_name=$JOB_NAME&build_url=$BUILD_URL" http://axiacore.com/build/set
