#!/usr/bin/python3
# Script that deletes out-of-date archives, using the function do_clean:

from fabric.api import run, local, env

env.hosts = ["104.196.221.76", "18.234.234.222"]


def do_clean(number=0):
    if (number == '0' or number == '1'):
        number = int(2)
    else:
        number = int(number) + 1
    if number < 0:
        return
    lista = local("ls -t versions/ | tail -n+{}".format(number), capture=True)
    lista = str(lista)
    lista = lista.split("\n")

    if (len(lista) > 0 and lista[0] != ""):
        for l in lista:
            local("rm versions/"+l)
            m = l.split(".")
            m = m[0]
            print("rm -rf /data/web_static/releases/"+m+"/")
            run("rm -rf /data/web_static/releases/"+m+"/")
