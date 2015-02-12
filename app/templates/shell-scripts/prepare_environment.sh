#!/bin/bash
# This script prepares your environment for the first time creating the
# database for you, the virtualenv and puts your local_settings

# You are using postgresql, virtualenv and you have every requisite needed to
# work in your project

if [ "$#" -ne 2 ]; then
  echo 'Usage: '$0 'APP_NAME(Your application name)"' >&2
  exit 1
fi

APPNAME=$1
PATH=$2

cd $PATH
if [ ! -e "requirements.txt"]; then
  echo 'Make sure you are running the script inside your repository structure'
fi

# Create Database
createdb -O django $1

# Create virtualenv
mkvirtualenv $APPNAME'_app'

# install requirements
. ~/.virtualenvs/$APPNAME'_app'/bin/activate
pip install -r requirements.txt
