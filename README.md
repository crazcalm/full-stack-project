# full-stack-project
I would like to try my hand at creating a professional piece of work.


##VM Ports
* Dev: localhost:8888

##Useful commands
* Run App
    * python run.py -h (Command line interface)

* Setup Virtualenv
    * python Provision/python_env/setup_virtualenv.py

* Run Tests
    * (From the app directory run) python -m unittest discover -v -b tests/

* Run Coverage
    * python -m coverage report -m --include="./*"

##Initializing the Environment
    1. clone git@github.com:crazcalm/full-stack-project.git

    2. cd into repo

    3. vagrant up --provision

    4. vagrant ssh

    5. sudo python3 /vagrant/Provision/python_env/setup_virtualenv.py

    6. bash /vagrant/Provision/python_env/setup_pyenv.sh

    7. source ~/.bashrc

    8. pyenv install 3.4.3

    9. pyenv global 3.4.3

    10. cd /vagrant/app

    11. mkvirtualenv -p python flask_app

    12. pip install -r requirements.txt

##Initializing the Environment Explained
    - Step 3: Runs the provisioning script Privision/dev.sh

    - Steps 5: Setting up virtualenv. I automated the steps found in
      https://nextdime.wordpress.com/2014/07/03/how-to-set-up-python-development-environment-ubuntu-14-04/

    - Step 6: Setting up pyenv.
        - http://amaral-lab.org/resources/guides/pyenv-tutorial

    - Step 7: Steps 5 and 6 add code to the bashrc file. This command activates
              that code.

    - Step 8: Installs python 3.4.3

    - Step 9: Sets python 3.4.3 as the global python

    - Step 11: Creates a virtualenv using python3 called flask_app.
      - `deactivate` ==> Exits virtualenv
      - `workon` ==> Will list the virtualenvs that you have
      - `work on flask_app` ==> Will activate the flask_app virtualenv

    - Step 9: Installs the required python packages into the virtualenv

## Initializing the Environment Warnings
    Step 5 should only be ran once. If it is ran more than once, then
    multiple line of the same code is appended to your bashrc file. The duplicate
    lines of code need to be removed before the `source ~/.bashrc` will work.


##Helpful blog posts!
* https://realpython.com/blog/python/kickstarting-flask-on-ubuntu-setup-and-deployment/
* https://nextdime.wordpress.com/2014/07/03/how-to-set-up-python-development-environment-ubuntu-14-04/

##Stack Overflow FTW
* Nginx:
    * http://stackoverflow.com/questions/17859653/nginx-not-running-with-no-error-message

* Cannot call source command from python subprocess module:
    * http://stackoverflow.com/questions/7040592/calling-the-source-command-from-subprocess-popen

* Using unittest to capture stdout:
    * http://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python

##Cool stuff
* pyenv
    * Allows me to install multiple versions of python at once.
    * http://amaral-lab.org/resources/guides/pyenv-tutorial

* tox
    - Will run your test in multiple environments.