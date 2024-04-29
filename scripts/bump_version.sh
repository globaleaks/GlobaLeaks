#!/bin/bash
# An utility script to bump project version
# across multiple files
# The file is expected to be run from the project's root directory
#
set -e

latest_tag=`git for-each-ref --sort=-taggerdate --count=1 --format '%(tag)' refs/tags`

current_version=${latest_tag:1}

if [[ "$1" != "" ]] && [[ "$1" != "$current_version" ]]; then

	echo "Updating version to v$1 from v$current_version"
	
	root_dir=`pwd`

	sed -i "s/^__version__ =.*/__version__ = '$1'/g" backend/globaleaks/__init__.py
	
	sed -i "s/^\"version\":.*/\"version\": \"$1\",/g" client/package.json

	sed -i "s/^softwareVersion:.*/softwareVersion: $1/g" publiccode.yml

	sed -i "s/^releaseDate:.*/releaseDate: '$(date +'%Y-%m-%d')'/g" publiccode.yml
	
	echo -e "Changes in version $1\n\t\tTODO\n$(cat CHANGELOG)" > CHANGELOG

else
	echo -e "Please specify a version other than the current version.\nCurrent Version: $current_version"
	exit 1
fi
