#!/bin/sh

# Check argument count
if [ "$#" -ne 2 ]; then
    echo "Usage: <path-to-extensions-dir> <interpreter>"
    exit
fi

# Remove .inx files using python interpreter
for match in `grep -RPoi "interpreter=\"$2\">\K([^ <]+)" "$1"/*.inx`; do
    manifest=${match%%:*}
    script=${match:${#manifest}+1}

    rm -f "$manifest"
    rm -f "$1"/"$script"
done
