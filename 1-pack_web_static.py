#!/usr/bin/python3
# Script that generates a .tgz archive from the contents of the web_static 
# folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local
from os import stat
from datetime import datetime


def do_pack():
    try:
        stat("versions")
    except:
        local("mkdir versions")
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_" + time + ".tgz"
        local("tar -cvzf " + name + " web_static")
        return name
    except:
        return None
