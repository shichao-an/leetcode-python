#!/bin/bash

usage="./makedir.sh title [...]"
[ "$#" -eq 0 ] && { echo "$usage"; exit 1; }

scriptdir=$(dirname "$0")
newdir="$scriptdir/$(echo "$@" | tr 'A-Z ' 'a-z_')"

[ -d "$newdir" ] && { echo "This directory already exists"; exit 1; } 

echo "Creating new directory $newdir ..."
mkdir "$newdir"
