#!/bin/python3

from fabric.api import *
from fabric.contrib import files
from fabric.operations import put
import os


class FabricException(Exception):
    pass


### Fabric ENVIRONMENT VARS ###
env.abort_exception = FabricException
env.user   = "ubuntu"
# env.password = os.environ["KVM_GUEST_PASS"]
env.key_filename = '~/aws_keys/savelono.pem'

# Avoids storing host to git
env.hosts = [os.environ['STBERNPBX']]

env.port = "22"
env.command_timeout = 600
env.connection_attempts = 3
env.warn_only = True


def deploy():
    """
    update git repo, update server
    """
    with lcd("../st-bern-asterisk-base"):
        local("git add .")
        local('git commit -m "ADD    Automted Fabric Commit"')
        local("git push")

        with cd("/etc/asterisk/"):
            put("*.conf","./",use_sudo=True)
        
    with lcd("../asterisk-users/auto"):

        with cd("/etc/asterisk/"):
            put("*.auto.conf","./",use_sudo=True)

def  voicemail():
    """
    get vm passwords
    """
    sudo("sed -n -e '/\[default\]/,/\[/ p' /etc/asterisk/voicemail.conf | grep '200 =>' | awk '{ print $3 }' | cut -d ',' -f1")