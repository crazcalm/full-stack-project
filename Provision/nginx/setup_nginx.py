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
    "testing": False
}


def create_cmds(config):
    """
    This function creates the commands needed for the
    ngnix setup.
    """
    cmd1 = "rm /etc/nginx/sites-enabled/default"
    cmd2 = (
        "echo '$(cat {})' > "
        "/etc/nginx/sites-available/flask_project"
    ).format(congig.app_config))

    cmd3 = ("ln -s /etc/nginx/sites-available/flask_project "
        "/etc/nginx/sites-enabled/flask_project")
    cmd4 = "/etc/init.d/nginx restart"

    results = [cmd1, cmd2, cmd3, cmd4]
    return results

def setup_nginx(config):
    commands = create_cmds(config)
    for cmd in commands:
        subprocess.call(cmd, shell=True)

def main(config):
    if os.exist(config.defualt_file):
        setup_nginx(config)
        print("The setup process has finished")

    else:
        print("Nginx has already been setup.")
        subprocess.call("/etc/init.d/nginx restart", shell = True)
