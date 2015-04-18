"""
I need a script that checks to see of nginx has been setup.
If not, then set it up.

Basic bash commands:
--------------------

#/etc/init.d/nginx start
#rm /etc/nginx/sites-enabled/default
#echo "$(cat /vagrant/Provision/nginx/flask_project)" > /etc/nginx/sites-available/flask_project
#ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project
#/etc/init.d/nginx restart  # Restarting nginx
"""

import subprocess
import os


# Constants
NGINX = {
    "defualt_file": "/etc/nginx/sites-enabled/default",
    "app_config": "/vagrant/Provision/nginx/flask_project",
    "testing" : False
    }

def setup_nginx(config):
    cmd1 = "rm /etc/nginx/sites-enabled/default"
    cmd2 = "echo '$(cat {})' > /etc/nginx/sites-available/flask_project".format(congig.app_config)

def main(config):
    if os.exist(config.defualt_file):
        setup_nginx(config)