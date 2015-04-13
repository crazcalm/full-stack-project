#! /usr/bin/env bash

# update packages
apt-get update

# Basic installs
apt-get install -y git
apt-get install -y curl

# Personal installs
apt-get install fish -y
apt-get install -y sl
apt-get install -y tree