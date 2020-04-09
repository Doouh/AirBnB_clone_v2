#!/usr/bin/python3
# Script that distributes an archive to your web
# servers, using the function do_deploy

from fabric.api import env, put, run
from os import stat

env.hosts = ["104.196.221.76", "18.234.234.222"]


def do_deploy(archive_path):
    try:
        stat(archive_path)
    except:
        return False
    try:
        name = archive_path.split("/")
        name = name[1].split(".")
        name = name[0]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{}.tgz -C \
            /data/web_static/releases/{}/".format(name, name))
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name))
        print("New version deployed!")
        return True
    except:
        return False
