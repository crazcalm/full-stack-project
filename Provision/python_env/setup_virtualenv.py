"""
This file is dedicated to doing the heavy lifting when setting up virtualenv and virtualenvwrapper
on a new machine.
"""


import subprocess
import os


# constants
PROJECT_PATH = "/vagrant"

INSTRUCTIONS = {
    "check": "~/.virtualenvs",
    "testing": False,
    "bashrc_code": PROJECT_PATH + "/Provision/python_env/bashrc_code",
    "pip": "pip install virtualenv virtualenvwrapper",
    "bashrc_location": "~/.bashrc",
    "enable": "source ~/.bashrc",
    "install_ez_setup": "python " + PROJECT_PATH + "/Provision/python_env/ez_setup.py",
    "install_pip": "easy_install pip",
    "bash_script": PROJECT_PATH + "/Provision/python_env/setup_virtualenv.sh"
}


def setup_virtualenv(config):
    """
    The methos evokes all the needed shell commands.

    :param config: dict
    :return: None
    """
    if config["testing"]:
        print("Here is where the setup would be.")

    else:
        # Install ez_setup
        subprocess.call(config["install_ez_setup"], shell=True)

        # Install pip globally
        subprocess.call(config["install_pip"], shell=True)

        # Install the needed packages
        subprocess.call(config["pip"], shell=True)

        # Add code to bashrc file
        subprocess.call(
            "echo $(cat {}) >> {}".format(
                config["bashrc_code"],
                config["bashrc_location"]
            ),
            shell=True
        )


def main(config):
    """
    The method controls the logic of this script

    :param config: dict
    :return: None
    """
    if os.path.exists(config["check"]):
        print("Virtualenv has already been setup.")

    else:
        print("Started the virtualenv setup process.")
        setup_virtualenv(config)
        print("The Virtualenv setup has been completed!")
        print("To complete install run")
        print("\n\nsource ~/.bashrc")


if __name__ == '__main__':
    main(INSTRUCTIONS)
