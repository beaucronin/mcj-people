#!/bin/bash

mkdir -p images
mkdir -p profiles

python fetch.py > records.json
python hugoify.py
cd profiles
cp *.md ../../mcj/content/profiles/
cd ../images
cp * ../../mcj/static/img