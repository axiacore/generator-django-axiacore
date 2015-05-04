#!/bin/bash
# This script prepares your environment for the first time creating the
# database for you, the virtualenv and puts your local_settings

# You are using postgresql, virtualenv and you have every requisite needed to
# work in your project

if [ "$#" -ne 1 ]; then
  echo 'Usage: '$0 'APP_NAME(Your application name)"' >&2
  exit 1
fi

APPNAME=$1

if [ ! -e "requirements.txt" ]; then
  pwd
  echo 'Make sure you are running the script inside your repository structure'
fi

# Create Database
createdb -O django $APPNAME

# Create virtualenv
virtualenv ~/.virtualenvs/$APPNAME'_app'/

# install requirements
. ~/.virtualenvs/$APPNAME'_app'/bin/activate

~/.virtualenvs/$APPNAME'_app'/bin/pip install -r requirements.txt
