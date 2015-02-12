#!/bin/bash
# This script creates a repository in bitbucket
if [ "$#" -ne 5 ]; then
  echo 'Usage: '$0 'USER PASSWORD REPOSLUG URLKEYS "REPOSITORY DESCRIPTION"' >&2
  exit 1
fi

# You must provide your user, password, slug and small description for repository
# This will create the repository for the team Axiacore
USERNAME=$1
PASSWORD=$2
SLUG=$3
URLKEYS=$4
DESC=$5

REPO="https://api.bitbucket.org/2.0/repositories/axiacore/$SLUG"

# Create repository
CURLRESULT=$(curl -v -X POST -u $USERNAME:$PASSWORD -H "Content-Type: application/json" \
  $REPO -d "{\"scm\": \"git\", \"is_private\": \"true\", \"fork_policy\": \"no_forks\", \"description\": \"$DESC\", \"language\": \"python\", \"has_issues\": \"false\", \"has_wiki\": \"false\"}" 2>/dev/null)

if [[ $CURLRESULT == *"already exists"* ]]
then
  echo "The repository $SLUG already exists"
  exit 1
fi

# Get keys from provided URL
IFS=$'\r\n' GLOBIGNORE='*' :; LINES=($(curl $URLKEYS 2>/dev/null))
REPO="https://bitbucket.org/api/1.0/repositories/axiacore/$SLUG/deploy-keys"

# Authorize those keys
for KEY in "${LINES[@]}"
do
  CURLRESULT=$(curl -v --request POST --user $USERNAME:$PASSWORD \
  $REPO --header "Content-Type: application/json" --header "Accept: application/json" -d "{\"key\": \"$KEY\"}" 2>/dev/null)
done

