#!/usr/bin/python3
# Script that deletes out-of-date archives, using the function do_clean:

from fabric.api import put, run, local
from os import stat

env.hosts = ["104.196.221.76", "18.234.234.222"]


def do_clean(number=0):
    if (number == '0' or number == '1'):
        number = int(2)
    else:
        number = int(number) + 1
    lista = local("ls -t versions/ | tail -n+{}".format(number), capture=True)
    lista = str(lista)
    lista = lista.split("\n")

    for l in lista:
        local("rm versions/"+l)
        run("rm /data/web_static/releases/"+l)
