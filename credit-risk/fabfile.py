"""Fabric script run commands on a remote server.

Install Fabric to get started.

    pip install Fabric3
"""

from fabric.api import task, run, env, sudo, prompt

## Change this to IP address/hostname of your remote machine
env.hosts = ['ds00.pipal.in']

# change it to your name
env.user = 'root'

# Set a password
# env.password = open("password.txt").read().strip()

@task
def hello():
    run("echo hello")

@task
def ip():
    run("curl http://httpbin.org/ip")


