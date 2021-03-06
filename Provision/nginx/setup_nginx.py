"""
This file is dedicated to doing the heavy lifting when setting up
Ngnix.
"""

import subprocess
import os

# Constants
PROJECT_PATH = "/vagrant"

NGINX = {
    "defualt_file": "/etc/nginx/sites-available/default",
    "new_file_name": "/etc/nginx/sites-available/flask_project",
    "sim_link": "/etc/nginx/sites-enabled/flask_project",
    "app_config": PROJECT_PATH + "/Provision/nginx/flask_project",
    "restart": "/etc/init.d/nginx restart",
    "testing": False
}


def create_cmds(config):
    """
    This function creates the commands needed for the
    ngnix setup.
    """
    cmd1 = (
        "echo $(cat {}) > {}"
    ).format(config["app_config"], config["new_file_name"])

    cmd2 = (
        "ln -s {0} {1}"
    ).format(
        config["app_config"],
        config["sim_link"]
    )
    cmd3 = "{}".format(config["restart"])

    results = [cmd1, cmd2, cmd3]
    return results


def setup_nginx(config):
    """
    This method evokes all of the shell commands located in the config object.

    :param config: dict
    :return: None
    """
    commands = create_cmds(config)
    for index, cmd in enumerate(commands):
        if config["testing"]:
            print("Command {0}: {1}".format(index, cmd))
        else:
            subprocess.call(cmd, shell=True)


def main(config):
    """
    This method deals with the logic of setting up nginx

    :param config: dict
    :return: None
    """
    if os.path.exists(config["defualt_file"]):
        print("You need to delete {}".format(config["defualt_file"]))

    if not os.path.exists(config["new_file_name"]):
        print("Starting the Nginx setup process")
        setup_nginx(config)
        print("The setup process has finished")

    else:
        print("Nginx has already been setup.")

if __name__ == '__main__':
    main(NGINX)
