from __future__ import with_statement
import os, sys, time, getpass

from fabric.api import *
from fabric.colors import red, green, blue, cyan, magenta, white, yellow
from fabric.api import put, run, settings, sudo
from fabric.operations import prompt

env.REMOTE_CODEBASE_PATH        = '/home/ubuntu/website'
env.VENDOR_PATH                 = "/home/ubuntu/code"
env.BUILD_FOLDER                = "/home/ubuntu/build"
env.PROJECT_PATH                = os.path.dirname(os.path.abspath(__file__))
env.VENUS_PROJECT_PATH          = '/home/ubuntu/website'
env.BRANCH_NAME                 = 'master'
env.user                        = 'ubuntu'
env.key_filename                = '/Users/%s/.ssh/id_rsa' % getpass.getuser()

env.roledefs = {
    'master' : ['52.71.97.249'],
}

def install_deploy_tools():
    sudo('add-apt-repository -y ppa:chris-lea/node.js')
    sudo('apt-get update')
    sudo('apt-get install -y nodejs')
    run('curl -L https://npmjs.org/install.sh | sudo sh')
    sudo("npm install -g uglify-js")
    sudo("npm -g install yuglify")
        
def setup_installs():
    """ Installs apt-get packages """
    packages = [
        'build-essential',
        'gcc',
        'libreadline-dev',
        'libpcre3-dev',
        'libssl-dev',
        'sysstat',
        'iotop',
        'git',
        'python-dev',
        'locate',
        'python-software-properties',
        'software-properties-common',
        'libpcre3-dev',
        'libncurses5-dev',
        'libdbd-pg-perl',
        'libssl-dev',
        'make',
        'libyaml-0-2',
        'python-setuptools',
        'python-yaml',
        'python-numpy',
        'python-scipy',
        'curl',
        'libjpeg8',
        'libjpeg62-dev',
        'libfreetype6',
        'libfreetype6-dev',
        'python-imaging',
        'python-pip',
        'libsqlite3-dev',
    ]
    sudo('apt-get -y update')
    sudo('DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes upgrade')
    sudo('DEBIAN_FRONTEND=noninteractive apt-get -y --force-yes install %s' % ' '.join(packages))

    with settings(warn_only=True):
        sudo("ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib")
        sudo("ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib")
        sudo("ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib")

    with settings(warn_only=True):
        sudo('mkdir -p %s' % env.VENDOR_PATH)
        sudo('chown %s.%s %s' % (env.user, env.user, env.VENDOR_PATH))
