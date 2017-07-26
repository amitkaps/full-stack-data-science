"""Python interface to classic unix utilities.
"""
import subprocess

def fortune(short=False):
    """Returns the output of classic ``fortune`` command in unix.
    """
    cmd = ["fortune"]
    if short:
        cmd.append("-s")
    output = subprocess.check_output(cmd)
    return output.decode('ascii', 'ignore')


def banner(message):
    """Returns the message as a large banner using class unix command ``banner``.
    """
    cmd = ["banner", message]
    output = subprocess.check_output(cmd)
    return output.decode('ascii', 'ignore')


def _cowsay(message, cowfile=None, cmdname='cowsay'):
    cmd = [cmdname]
    if cowfile:
        cmd.append("-f")
        cmd.append(cowfile)
    cmd.append(message)
    output = subprocess.check_output(cmd)
    return output.decode('ascii', 'ignore')


def cowsay(message, cowfile=None):
    """configurable speaking cow, a classic unix program.
    """
    return _cowsay(message, cowfile=cowfile, cmdname="cowsay")


def cowthink(message, cowfile=None):
    """configurable thinking cow, a classic unix program.
    """
    return _cowsay(message, cowfile=cowfile, cmdname="cowthink")
