#!/usr/bin/python3
# Script that deletes out-of-date archives, using the function do_clean:

from fabric.api import run, local, env

env.hosts = ["104.196.221.76", "18.234.234.222"]


def do_clean(number=0):
    number = int(number)
    local("ls -d -ltr versions/ | tail -n + {} | xargs -d '\n' rm -f --".format(2 if number < 1 else number + 1))
    run("ls -d -ltr /data/web_static/releases/ | tail -n + {} | xargs -d '\n' rm -f --".format(2 if number < 1 else number + 1))
