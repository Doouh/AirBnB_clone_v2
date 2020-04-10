#!/usr/bin/python3
# Script that creates and distributes an archive to your
# web servers, using the function deploy

from fabric.api import local, runs_once, env, put, run
from os import stat, path
from datetime import datetime

_path = None
env.hosts = ["104.196.221.76", "18.234.234.222"]

@runs_once
def do_pack():
    try:
        stat("versions")
    except:
        local("mkdir versions")
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_" + time + ".tgz"
        print("Packing web_static to " + name)
        local("tar -cvzf " + name + " web_static")
        filesize = path.getsize(name)
        print("web_static packed: " + name + " -> " + str(filesize) + "Bytes")
        return name
    except:
        return None

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

def deploy():
    global _path
    if _path is None:
        _path = do_pack()
    if _path is None:
        return False
    return do_deploy(_path)
