#!/bin/bash

set -e

function setup {
    echo ":: Cleaning old posts ..."
    rm $(pwd)/bitwig-resources/content/posts/*.md
}

function run {

    python main.py
    cd ./bitwig-resources
    hugo
    scp -r $(pwd)/public/* ditr:/www/bitwig-resources
    cd ..
}


function main {
    while true; do
        echo ":: Running ..."
        setup & run
        echo ":: Sleeping ..."
        sleep 30
    done
}

main