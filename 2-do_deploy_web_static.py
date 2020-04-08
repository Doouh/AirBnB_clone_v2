#!/usr/bin/python3
# Script that distributes an archive to your web servers, using the function do_deploy

from fabric.api import env, put, run
from os import stat

env.hosts = ['104.196.221.76', '18.234.234.222']

def do_deploy(archive_path):
    try:
        stat(archive_path)
    except:
        return False
    name = archive_path.replace(".", "/")
    name = name.split("/")
    name = name[1]
    try:
        put(archive_path, "/tmp/")
        print("1")
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        print("2")
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(name, name))
        print("3")
        run("rm /tmp/{}.tgz".format(name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))
        print("New version deployed!")
        return True
    except:
        return False