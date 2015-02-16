#!/bin/bash
pip install -r requirements.txt

./manage.py test --failfast
