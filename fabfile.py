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
env.key_filename = '~/aws_keys/stbern.pem'

# Avoids storing host to git
env.hosts = [os.environ('STBERNPBX')]

env.port = "22"
env.command_timeout = 600
env.connection_attempts = 3
env.warn_only = True
