# full-stack-project
I would like to try my hand at creating a professional piece of work.


##VM Ports
* Dev: localhost:8888

##Useful commands
* Run App
    * python3 run.py -h (Command line interface)

* Setup Virtualenv
    * python3 Provision/python_env/setup_virtualenv.py

* Run Tests
    * (From the app directory run) python3 -m unittest discover -v tests/

* Run Coverage
    * python3 -m coverage report -m --include="./*"

##Initializing the Environment
    1. clone git@github.com:crazcalm/full-stack-project.git
    
    2. cd into repo
    
    3. vagrant up --provision
    
    4. vagrant ssh
    
    5. sudo python3 /vagrant/Provision/python_env/setup_virtualenv.py
    
    6. source ~/.bashrc
    
    7. cd /vagrant/app
    
    8. mkvirtualenv -p /usr/bin/python3 flask_app
    
    9. pip install -r requirements.txt
    
##Initializing the Environment Explained
    - Step 3: Runs the provisioning script Privision/dev.sh
    
    - Steps 5-6: Setting up virtualenv. I automated the steps found in
      https://nextdime.wordpress.com/2014/07/03/how-to-set-up-python-development-environment-ubuntu-14-04/
      
    - Step 8: Creates a virtualenv using python3 called flask_app.
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

##Cool stuff
* pyenv?
    - Allows me to install multiple versions of python at once.
* pi-dev?
    - Proxy server for pypi that will allow me to cache previous install and
      host my own pip installable files (If needed)
* tox
    - Will run your test in multiple environments.