"""Fabric script run commands on a remote server.

Install Fabric to get started.

    pip install Fabric3

To list all available tasks:

    fab list

Run any task using the task name.

    fab hello
"""

from fabric.api import task, run, env, sudo, prompt, cd

## Change this to IP address/hostname of your remote machine
env.hosts = ['ds00.pipal.in']

# change it to your name
env.user = 'root'

# Set a password
# env.password = open("password.txt").read().strip()

ANACONDA_INSTALLER = "https://repo.continuum.io/archive/Anaconda3-4.4.0-Linux-x86_64.sh"
REPO_URL = "https://github.com/amitkaps/full-stack-data-science.git"

@task
def hello():
    run("echo hello")

@task
def ip():
    run("curl http://httpbin.org/ip")

@task
def provision():
    install_anaconda()

def install_anaconda():
    run("wget -nv -O /tmp/anaconda-installer.sh " + ANACONDA_INSTALLER)
    run("bash /tmp/anaconda-installer.sh -b -p /usr/local/anaconda3")
    run("ln -s /usr/local/anaconda3/bin/python /usr/bin/")

@task
def info():
    run("date")
    run("w")
    run("/usr/local/anaconda3/bin/python --version")
    run("ls")

@task
def clone():
    run("git clone " + REPO_URL)

@task
def install_python_packages():
    with cd("/root/full-stack-data-science/credit-risk"):
        run("/usr/local/anaconda3/bin/pip install -r requirements.txt")
