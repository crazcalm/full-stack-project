#! /usr/bin/env bash

# update packages
apt-get update

# Basic installs
apt-get install -y git
apt-get install -y curl
apt-get install -y nginx

# Ensuring that python3 is intalled
apt-get install -y python3
apt-get install -y python3-dev

# Python installs
apt-get install -y python3-pip
apt-get install -y supervisor  # Restarts the application when a change is made.

# Virtualenv installs
apt-get install -y build-essential
apt-get install -y python-dev
apt-get install -y libsqlite3-dev
apt-get install -y libreadline6-dev
apt-get install -y libgdbm-dev
apt-get install -y zlib1g-dev
apt-get install -y libbz2-dev
apt-get install -y sqlite3
apt-get install -y zip


# Personal installs
apt-get install fish -y
apt-get install -y sl
apt-get install -y tree

# App requirments.txt installs
python3 -m pip install -r /vagrant/app/requirements.txt


# Setting up nginx
python3 /vagrant/Provision/nginx/setup_nginx.py

# Setting up virtualenv
python3 /vagrant/Provision/python_env/setup_virtualenv.py