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
    ).format(config["app_config"])

    cmd3 = ("ln -s /etc/nginx/sites-available/flask_project "
            "/etc/nginx/sites-enabled/flask_project")
    cmd4 = "/etc/init.d/nginx restart"

    results = [cmd1, cmd2, cmd3, cmd4]
    return results


def setup_nginx(config):
    commands = create_cmds(config)
    for index, cmd in enumerate(commands):
        if config["testing"]:
            print("Command {0}: {1}".format(index, cmd))
        else:
            subprocess.call(cmd, shell=True)


def main(config):
    if os.path.exists(config["defualt_file"]):
        setup_nginx(config)
        print("The setup process has finished")

    else:
        print("Nginx has already been setup.")

if __name__ == '__main__':
    main(NGINX)
