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