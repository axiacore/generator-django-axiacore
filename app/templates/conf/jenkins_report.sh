#!/bin/bash
pip install -r requirements.txt

./manage.py test --jenkins

curl -fsSL https://raw.github.com/AxiaCore/axiacore_utils/master/jenkins/jshint_report.sh | bash

curl -fsSL https://raw.github.com/AxiaCore/axiacore_utils/master/jenkins/cloc_report.sh | bash
