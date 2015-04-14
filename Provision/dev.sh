#! /usr/bin/env bash

# update packages
apt-get update

# Basic installs
apt-get install -y git
apt-get install -y curl
apt-get install -y nginx

# Python installs
apt-get install -y python3-pip

# Personal installs
apt-get install fish -y
apt-get install -y sl
apt-get install -y tree

# App requirments.txt installs
python3 -m pip install -r /vagrant/app/requirements.txt