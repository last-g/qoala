#!/bin/bash

PROJECT=/qoala/
# Installing deps
source ${PROJECT}/deploy/common.sh
${CURRENT}/install_dependencies.sh

# Installing supervisor
ln -s ${PROJECT}/etc/supervisor/qoala.conf /etc/supervisor/conf.d/

# Migrating data
${PROJECT}/manage.py syncdb --migrate

# Setting up user
${PROJECT}/manage.py loaddata develop_superuser.json

# Restarting supervisor to apply changes
sudo /etc/init.d/supervisor stop
sudo /etc/init.d/supervisor start
sudo supervisorctl restart all

