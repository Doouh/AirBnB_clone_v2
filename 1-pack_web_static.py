#!/usr/bin/python3
# Script that generates a .tgz archive from the contents of the web_static 
# folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local, runs_once
from os import stat, path
from datetime import datetime


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
