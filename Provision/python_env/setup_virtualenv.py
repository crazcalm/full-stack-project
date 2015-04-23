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
    "install_pip": "easy_install pip"
}


def check_if_installed():
    result = True

    check = subprocess.call("workon", shell=True)

    if check == 127:
        result = False

    print(check, result, type(check))
    return result


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
        print("echo -e $(cat {}) >> {}".format(config["bashrc_code"],config["bashrc_location"]))
        subprocess.call(
            "echo $(cat {}) >> {}".format(
                config["bashrc_code"],
                config["bashrc_location"]
            ),
            shell=True
        )

        # Enable Virtualenv
        subprocess.call(config["enable"], shell=True)


def main(config):
    if check_if_installed():
        print("Virtualenv has already been setup.")

    else:
        print("Started the virtualenv setup process.")
        setup_virtualenv(config)
        print("The Virtualenv setup has been completed!")


if __name__ == '__main__':
    main(INSTRUCTIONS)
