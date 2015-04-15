#! /usr/bin/env bash

# update packages
apt-get update

# Basic installs
apt-get install -y git
apt-get install -y curl
apt-get install -y nginx

# Python installs
apt-get install -y python3-pip
apt-get install -y supervisor  # Restarts the application when a change is made.

# Personal installs
apt-get install fish -y
apt-get install -y sl
apt-get install -y tree

# App requirments.txt installs
python3 -m pip install -r /vagrant/app/requirements.txt

# I can only run the below commands once
# I need to externalize this.
# Ngnix python setup
#/etc/init.d/nginx start
#rm /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.copy
#echo "$(cat /vagrant/Provision/nginx/flask_project)" > /etc/nginx/sites-available/flask_project
#ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project
#/etc/init.d/nginx restart  # Restarting nginx