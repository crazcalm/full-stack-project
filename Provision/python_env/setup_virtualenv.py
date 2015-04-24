import subprocess
import os


# constants
INSTRUCTIONS = {
    "check": "/vagrant/.virtualenvs",
    "testing": False,
    "bashrc_code": "/vagrant/Provision/python_env/bashrc_code",
    "pip": "pip install virtualenv virtualenvwrapper",
    "bashrc_location": "~/.bashrc",
    "enable": "source ~/.bashrc",
    "install_ez_setup": "python /vagrant/Provision/python_env/ez_setup.py",
    "install_pip": "easy_install pip",
    "bash_script": "/vagrant/Provision/python_env/setup_virtualenv.sh"
}


def setup_virtualenv(config):
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
        input("pause/n/n")
        print("echo -e $(cat {}) >> {}".format(
            config["bashrc_code"],
            config["bashrc_location"])
        )
        subprocess.call(
            "echo $(cat {}) >> {}".format(
                config["bashrc_code"],
                config["bashrc_location"]
            ),
            shell=True
        )

        subprocess.call(
            "bash {}".format(
                config["bash_script"]
            ),
            shell=True
        )


def main(config):
    if os.path.exists(config["check"]):
        print("Virtualenv has already been setup.")

    else:
        print("Started the virtualenv setup process.")
        setup_virtualenv(config)
        print("The Virtualenv setup has been completed!")
        #print("To complete install run")
        #print("\n\nsource ~/.bashrc")


if __name__ == '__main__':
    main(INSTRUCTIONS)
