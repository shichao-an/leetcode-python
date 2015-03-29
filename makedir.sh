#!/bin/bash

USAGE="./makedir.sh title [...]"

[ "$#" -eq 0 ] && {
    echo "$USAGE"
    exit 1
}

SCRIPTDIR=$(dirname "$0")
NEWDIR="$SCRIPTDIR/$(echo "$@" | tr 'A-Z ' 'a-z_' | tr -d "'")"

[ -d "$NEWDIR" ] && {
    echo "This directory already exists"
    exit 1
}

echo "Creating new directory $NEWDIR ..."
mkdir "$NEWDIR"
touch "$NEWDIR/solution.py"
