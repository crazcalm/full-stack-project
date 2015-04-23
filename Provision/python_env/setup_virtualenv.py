import subprocess
import os


# constants
INSTRUCTIONS = {
    "check": "/vagrant/.virtualenvs",
    "testing": False,
    "bashrc_command": """
    # Virtualenv code (Marcus's added this)
    if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
    fi
    """,
    "pip": "pip install virtualenv virtualenvwrapper",
    "bashrc_location": "/vagrant/.bashrc",
    "enable": "source /vagrant/.bashrc"
}


def setup_virtualenv(config):
    if config["testing"]:
        print("Here is where the setup would be.")

    else:
        # Install the needed packages
        subprocess.call(config["pip"], shell=True)

        # Add code to bashrc file
        subprocess.call(
            (config["bashrc_command"] + " >> " + config["bashrc_location"]),
            shell=True
        )

        # Enable Virtualenv
        subprocess.call(config["enable"], shell=True)


def main(config):
    if os.path.exists(config["check"]):
        print("Virtualenv has already been setup.")

    else:
        print("Started the virtualenv setup process.")
        setup_virtualenv(config)
        print("The Virtualenv setup has been completed!")


if __name__ == '__main__':
    main(INSTRUCTIONS)
