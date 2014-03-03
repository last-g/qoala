#!/bin/bash

source `dirname $0`/common.sh

sudo apt-get update
sudo apt-get install -y python python-pip supervisor # python-setuptools  nginx gunicorn
sudo pip install -r ${PROJECT}/requirements.txt
